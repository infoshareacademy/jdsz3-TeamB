select distinct partner
from wnioski
where partner is not null
;

with analiza_partnerow as (
   select w.id,
       w.jezyk,
       w.partner,
       date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) / 24.0 as dni_realziacji
from wnioski w, analizy_wnioskow aw
where w.id = aw.id_wniosku
and w.partner is not null
and date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) > 0
)
select jezyk,
       count(id) as liczba_wnioskow,
       partner,
       avg(dni_realziacji) as sredni_czas_realizacji,
       percentile_disc(0.5) within group (order by dni_realziacji) as mediana_dni,
       (avg(dni_realziacji)/
        percentile_disc(0.5) within group (order by dni_realziacji))::float as wspolczynnik_avg_med
from analiza_partnerow
group by partner,jezyk
having count(id) > 10
order by jezyk;
