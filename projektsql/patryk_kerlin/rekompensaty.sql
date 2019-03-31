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
       ) as wnioski_niewyplacone
from wnioski
group by 1
having count(1) > 10
