select distinct *
from o_operatorzy;


with wnioski_vs_analiza_prawna as (
SELECT w.id as wnioski_w_sadzie,
       w.jezyk as jezyk_wnioskow,
       ap.status_sad as status_wniosku_sad,
       ap.data_rozpoczecia as data_rozp,
       ap.data_wyslania_sad as data_wysl,
       ap.data_odp_sad as data_odp
FROM wnioski w
left join analiza_prawna ap on w.id = ap.id_wniosku
WHERE ap.status_sad is not null
ORDER BY w.jezyk
    ),
     roznica_rozpoczecie_odp as (
         SELECT jezyk_wnioskow as jezyk,
                CASE WHEN extract(day from (data_odp - data_rozp))::numeric <0
                    then extract(day from (data_odp - data_rozp))::numeric*-1
                    ELSE extract(day from (data_odp - data_rozp))::numeric
                    END as czas_realizacji
         FROM wnioski_vs_analiza_prawna
     ),
     sredni_czas_realizacji_wnioskow_sad as(
         SELECT jezyk, AVG(czas_realizacji) as sredni_czas_realizacji
         FROM roznica_rozpoczecie_odp
         GROUP BY jezyk
     ),
     ilosc_wnioskow_w_danym_jezyku as (
         SELECT jezyk_wnioskow, COUNT(wnioski_w_sadzie) as ilosc_wnioskow_w_jezyku
         FROM wnioski_vs_analiza_prawna
         GROUP BY jezyk_wnioskow
     ),
     zestawienie as (
         SELECT *
         FROM ilosc_wnioskow_w_danym_jezyku iwdj, sredni_czas_realizacji_wnioskow_sad scrws
         WHERE iwdj.jezyk_wnioskow = scrws.jezyk
         ORDER BY scrws.sredni_czas_realizacji DESC
     ),
     mediana_czas_realizaccji as (
         SELECT jezyk,
               PERCENTILE_DISC(0.5) within group ( order by czas_realizacji ) as mediana_czas_realizacji
         FROM roznica_rozpoczecie_odp
         GROUP BY jezyk
     ),
     percentyle_czas_realizacji as (
         SELECT jezyk,
               PERCENTILE_DISC(0.001) within group ( order by czas_realizacji ) as Q01,
               PERCENTILE_DISC(0.05) within group ( order by czas_realizacji ) as Q5,
               PERCENTILE_DISC(0.1) within group ( order by czas_realizacji ) as Q10,
               PERCENTILE_DISC(0.2) within group ( order by czas_realizacji ) as Q20,
               PERCENTILE_DISC(0.3) within group ( order by czas_realizacji ) as Q30,
               PERCENTILE_DISC(0.5) within group ( order by czas_realizacji ) as Mediana_Q50,
               PERCENTILE_DISC(0.7) within group ( order by czas_realizacji ) as Q70,
               PERCENTILE_DISC(0.8) within group ( order by czas_realizacji ) as Q80,
               PERCENTILE_DISC(0.9) within group ( order by czas_realizacji ) as Q90,
               PERCENTILE_DISC(0.95) within group ( order by czas_realizacji ) as Q95,
               PERCENTILE_DISC(0.99) within group ( order by czas_realizacji ) as Q99
         FROM roznica_rozpoczecie_odp
         GROUP BY jezyk
     ),
     zliczanie_czasow_realizacji as (
         SELECT x.jezyk_wnioskow, COUNT(x.wnioski_w_sadzie)
         FROM wnioski_vs_analiza_prawna x
         group by jezyk_wnioskow
         HAVING COUNT(wnioski_w_sadzie) > 0
     ),
     srednia_mediana as (
     SELECT z.jezyk as jezyk,
            z.ilosc_wnioskow_w_jezyku as ilosc_wnioskow,
            z.sredni_czas_realizacji as sredni_czas_realizacji,
            mcr.mediana_czas_realizacji as mediana_czasu_realizacji
     FROM zestawienie z, mediana_czas_realizaccji mcr
     WHERE z.jezyk_wnioskow = mcr.jezyk
         ORDER by z.sredni_czas_realizacji DESC, mcr.mediana_czas_realizacji
     )

SELECT *
FROM srednia_mediana;
