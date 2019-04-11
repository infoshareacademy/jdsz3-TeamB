-- zasady i główne zadania (git)

select distinct jezyk, count(1)
from wnioski
group by 1;

select distinct stan_wniosku
from wnioski;

select *
from wnioski w
join rekompensaty r on w.id = r.id_wniosku
join szczegoly_rekompensat sr on r.id = sr.id_rekompensaty;


select w.jezyk, w.stan_wniosku, count(1) as liczba_wnioskow
from wnioski w
join rekompensaty r on w.id = r.id_wniosku
join szczegoly_rekompensat sr on r.id = sr.id_rekompensaty
group by 1, 2;

select jezyk, count(1)
from wnioski
where kwota_rekompensaty < kwota_rekompensaty_oryginalna
group by 1
order by 1;

select w.jezyk, w.stan_wniosku, w.liczba_pasazerow, w.kwota_rekompensaty, sr.kwota
from wnioski w
join rekompensaty r on w.id = r.id_wniosku
join szczegoly_rekompensat sr on r.id = sr.id_rekompensaty
where w.kwota_rekompensaty <> sr.kwota
and w.liczba_pasazerow > 3;

select jezyk, count(1) as liczba_wnioskow,
       percentile_disc(0.5) within group (order by (kwota_rekompensaty/liczba_pasazerow)) as mediana_per_pasazer
from wnioski
where stan_wniosku like 'wypl%'
group by 1
order by 3 desc;

select distinct(jezyk), count(1), kwota_rekompensaty/liczba_pasazerow as kwota_wypl_per_pasazer,
       kwota_rekompensaty_oryginalna/liczba_pasazerow as kwota_oryg_per_pasazer
from wnioski
where stan_wniosku like 'wypl%'
and kwota_rekompensaty_oryginalna/liczba_pasazerow <> kwota_rekompensaty/liczba_pasazerow
group by 1, 3, 4
order by 3, 1 desc


select jezyk, min(kwota_rekompensaty/liczba_pasazerow) as min_kwota_per_pasazer, count(1)
from wnioski
where stan_wniosku like '%wypl%'
group by 1

with rozne_wnioski as (
       select jezyk,
              count(1)                            as liczba_wnioskow,
              count(case
                           when kwota_rekompensaty <> kwota_rekompensaty_oryginalna then id
                     end)                         as liczba_roznych_wnioskow,
              round(100 * count(case
                                       when kwota_rekompensaty <> kwota_rekompensaty_oryginalna then id
                     end) / count(1)::numeric, 2) as proc_roznych_wniosków
       from wnioski
       where lower(stan_wniosku) like 'wyp%'
       group by 1
)
select *
from rozne_wnioski
where proc_roznych_wniosków > 0;

select count(1), stan_wniosku
from wnioski
where jezyk = 'ro'
group by 2

select *
from wnioski w
full join rekompensaty r on w.id = r.id_wniosku
full join szczegoly_rekompensat sr on r.id = sr.id_rekompensaty
where stan_wniosku like 'zamk%'
and sr.id is not null

select *
from wnioski w
full join rekompensaty r on w.id = r.id_wniosku
full join szczegoly_rekompensat sr on r.id = sr.id_rekompensaty
where stan_wniosku like 'zamk%'

select jezyk, count(1) as liczba_wnioskow,
       count(case
         when stan_wniosku not like 'wyplacony' then id
         end
       ) as wnioski_niewyplacone,
       round((100.0*count(case
         when stan_wniosku not like 'wyplacony' then id
         end
       ))/count(1),2) as procent_wnioskow_niewyplaconych
from wnioski
group by 1
having count(1) > 10;

with sredni_czas as (
  select w.jezyk,
         avg(date_part('day', sr.data_otrzymania - w.data_utworzenia))::numeric as sredni_czas_oczekiwania_na_wyplate_rekompensaty
  from wnioski w
         full join rekompensaty r on w.id = r.id_wniosku
         full join szczegoly_rekompensat sr on r.id = sr.id_rekompensaty
  where stan_wniosku like 'wypl%'
    and date_part('day', sr.data_otrzymania - w.data_utworzenia) > 0
  group by 1
)
select jezyk, round(sredni_czas_oczekiwania_na_wyplate_rekompensaty,0) as sredni_czas_oczekiwania_na_wyplate_rekompensaty_w_dniach
from sredni_czas

with rozne_wnioski as (
       select jezyk,
              count(1) as liczba_wnioskow,
              count(case
                      when kwota_rekompensaty <> kwota_rekompensaty_oryginalna then id
                     end) as liczba_roznych_wnioskow,
              round(100 * count(case
                                 when kwota_rekompensaty <> kwota_rekompensaty_oryginalna then id
                     end) / count(1)::numeric, 2) as proc_rozniacych_sie_wniosków,
              kwota_rekompensaty_oryginalna-kwota_rekompensaty as roznica
       from wnioski
       where lower(stan_wniosku) like 'wyp%'
       group by 1, 5
)
select *
from rozne_wnioski
where proc_rozniacych_sie_wniosków > 0
order by 4 desc;

select jezyk, round(avg((kwota_rekompensaty_oryginalna/liczba_pasazerow)-(kwota_rekompensaty/liczba_pasazerow)),2)
from wnioski
where kwota_rekompensaty_oryginalna-kwota_rekompensaty > 0
group by 1


select stan_wniosku, count(1)
from wnioski
where jezyk like 'pl'
group by 1

with wnioski_wszystkie as (
  select jezyk, count(1) as liczba_wszystkich_wnioskow
  from wnioski
  group by 1
),
     wnioski_niewyplacone as (
       select jezyk, stan_wniosku, count(1) as liczba_wnioskow
       from wnioski
       where stan_wniosku not in ('wyplacony', 'zamkniety', 'nowy', 'akcja sadowa',
                                  'wyslany do operatora', 'analiza zaakceptowana',
                                  'wygrany w sadzie', 'zaakceptowany przez operatora')
       group by 1, 2
       order by 1, 2
     )
select wn.stan_wniosku, wn.jezyk, wn.liczba_wnioskow,
       round(100 * ((wn.liczba_wnioskow)::numeric / ww.liczba_wszystkich_wnioskow),2) as procent_wnioskow
from wnioski_niewyplacone wn
full join wnioski_wszystkie ww on wn.jezyk = ww.jezyk
where wn.jezyk is not null
and wn.liczba_wnioskow > 20
order by 1, 2
