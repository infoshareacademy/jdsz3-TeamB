select jezyk, count(1) as liczba_wnioskow,
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

with rozne_wnioski as (
       select jezyk,
              count(1) as liczba_wnioskow,
              count(case
                      when kwota_rekompensaty <> kwota_rekompensaty_oryginalna then id
                     end) as liczba_roznych_wnioskow,
              round(100 * count(case
                                 when kwota_rekompensaty <> kwota_rekompensaty_oryginalna then id
                     end) / count(1)::numeric, 2) as proc_rozniacych_sie_wniosków
       from wnioski
       where lower(stan_wniosku) like 'wyp%'
       group by 1
)
select *
from rozne_wnioski
where proc_rozniacych_sie_wniosków > 0;

