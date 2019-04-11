-- Min, max , q1, mediana oraz q3 dla wniosków wypłaconych per pasażer

select jezyk, count(1) as liczba_wnioskow_wyplaconych,
       min(kwota_rekompensaty/liczba_pasazerow) as min_kwota_per_pasazer,
       percentile_disc(0.25) within group (order by (kwota_rekompensaty/liczba_pasazerow)) as q1_per_pasazer,
       percentile_disc(0.5) within group (order by (kwota_rekompensaty/liczba_pasazerow)) as mediana_per_pasazer,
       percentile_disc(0.75) within group (order by (kwota_rekompensaty/liczba_pasazerow)) as q3_per_pasazer,
       max(kwota_rekompensaty/liczba_pasazerow) as max_kwota_per_pasazer
from wnioski
where stan_wniosku like 'wypl%'
and kwota_rekompensaty > 0
group by 1
having count(1) > 10
order by 5 desc;

-- Procent wniosków, gdzie kwota wypłacona różni się od wnioskowanej

with rozne_wnioski as (
       select jezyk,
              count(1) as liczba_wnioskow,
              count(case
                      when kwota_rekompensaty <> kwota_rekompensaty_oryginalna then id
                     end) as liczba_roznych_wnioskow,
              round(100 * count(case
                                 when kwota_rekompensaty <> kwota_rekompensaty_oryginalna then id
                     end) / count(1)::numeric, 2) as proc_rozniacych_sie_wnioskow
       from wnioski
       where lower(stan_wniosku) like 'wyp%'
       group by 1
)
select *
from rozne_wnioski
where proc_rozniacych_sie_wnioskow > 0
order by 4;

-- Procent wniosków wypłaconych, odrzuconych oraz oczekujących na decyzję wg. języka

with odrzucone as (
  select jezyk, count(1) as liczba_wnioskow,
         count(case
                 when stan_wniosku not in ('wyplacony', 'zamkniety', 'nowy', 'akcja sadowa',
                                           'wyslany do operatora', 'analiza zaakceptowana',
                                           'wygrany w sadzie', 'zaakceptowany przez operatora') then id
           end
           )                 as wnioski_odrzucone,
         round((100.0 * count(case
                                when stan_wniosku not in ('wyplacony', 'zamkniety', 'nowy', 'akcja sadowa',
                                                          'wyslany do operatora', 'analiza zaakceptowana',
                                                          'wygrany w sadzie', 'zaakceptowany przez operatora') then id
           end
           )) / count(1), 2) as procent_wnioskow_odrzuconych
  from wnioski
  group by 1
  having count(1) > 10
  order by 4
),
     wyplacone as (
       select jezyk, count(1) as liczba_wnioskow,
         count(case
                 when stan_wniosku like 'wyplacony' then id
           end
           )                 as wnioski_wyplacone,
         round((100.0 * count(case
                                when stan_wniosku like 'wyplacony' then id
           end
           )) / count(1), 2) as procent_wnioskow_wyplaconych
  from wnioski
  group by 1
  having count(1) > 10
  order by 4
     ),
     oczekujace as (
       select jezyk, count(1) as liczba_wnioskow,
       count(case
         when stan_wniosku in ('akcja sadowa', 'nowy', 'wyslany do operatora',
                              'analiza zaakceptowana', 'wygrany w sadzie',
                              'zaakceptowany przez operatora') then id
         end
       ) as wnioski_oczekujace,
       round((100.0*count(case
         when stan_wniosku in ('akcja sadowa', 'nowy', 'wyslany do operatora',
                              'analiza zaakceptowana', 'wygrany w sadzie',
                              'zaakceptowany przez operatora') then id
         end
       ))/count(1),2) as procent_wnioskow_oczekujacych
from wnioski
group by 1
having count(1) > 10
order by 4
     ),
     jezyki as (
       select distinct jezyk
       from wnioski
     )
select j.jezyk, w.liczba_wnioskow, w.wnioski_wyplacone, w.procent_wnioskow_wyplaconych,
       o.wnioski_odrzucone, o.procent_wnioskow_odrzuconych,
       o2.wnioski_oczekujace, o2.procent_wnioskow_oczekujacych
from jezyki j
join wyplacone w on j.jezyk = w.jezyk
join odrzucone o on j.jezyk = o.jezyk
join oczekujace o2 on j.jezyk = o2.jezyk;


-- Średni czas oczekiwania na wypłatę rekompensaty

with sredni_czas as (
  select w.jezyk,
         avg(date_part('day', sr.data_otrzymania - w.data_utworzenia))::numeric as sredni_czas_oczekiwania_na_wyplate_rekompensaty
  from wnioski w
         join rekompensaty r on w.id = r.id_wniosku
         join szczegoly_rekompensat sr on r.id = sr.id_rekompensaty
  where stan_wniosku like 'wypl%'
    and date_part('day', sr.data_otrzymania - w.data_utworzenia) > 0
  group by 1
)
select jezyk, round(sredni_czas_oczekiwania_na_wyplate_rekompensaty,0) as sredni_czas_oczekiwania_na_wyplate_rekompensaty_w_dniach
from sredni_czas
order by 2 desc;

-- Procent wniosków odrzuconych wg. stanu i języka

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
       round(100 * ((wn.liczba_wnioskow)::numeric / ww.liczba_wszystkich_wnioskow),2)
         as procent_wnioskow_odrzuconych
from wnioski_niewyplacone wn
full join wnioski_wszystkie ww on wn.jezyk = ww.jezyk
where wn.jezyk is not null
and wn.liczba_wnioskow > 9
order by 1, 4, 2;


