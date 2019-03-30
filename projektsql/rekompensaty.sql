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
       percentile_disc(0.5) within group (order by (kwota_rekompensaty/liczba_pasazerow)) as mediana,
       round(avg(kwota_rekompensaty/liczba_pasazerow),0) as srednia
from wnioski
where stan_wniosku like 'wypl%'
group by 1
order by 1;

