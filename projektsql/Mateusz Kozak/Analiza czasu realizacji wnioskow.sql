select distinct *
from analiza_operatora;

select w.id,
       w.jezyk,
       to_char(ap.data_rozpoczecia, 'YYYY-MM-DD') as data_rozp_sad,
       to_char(ap.data_wyslania_sad, 'YYYY-MM-DD') as data_wys_sad,
       to_char(ap.data_odp_sad, 'YYYY-MM-DD') as data_odp_sad,
       to_char(ao.data_wysylki, 'YYYY-MM-DD') as data_wys_operator,
       to_char(ao.data_odpowiedzi, 'YYYY-MM-DD') as data_odp_operator,
       to_char(aw.data_utworzenia, 'YYYY-MM-DD') as data_utworzenia_wnioski,
       to_char(aw.data_zakonczenia,'YYYY-MM-DD') as data_zakonczenia_wnioski,
       to_char(w.data_utworzenia, 'YYYY-MM-DD') as data_utw_wniosek
from wnioski w, analiza_prawna ap, analiza_operatora ao, analizy_wnioskow aw
where w.id = ap.id_wniosku
and ap.id_wniosku = ao.id_wniosku
and w.id = aw.id_wniosku
order by jezyk
limit 5;

select w.id as wniosek,
       w.jezyk,
       ao.status_odp as analiza_operatora_status,
       aw.status as analiza_wnioskow_status,
       ap.status as analiza_prawna_status,
       ap.status_sad as analiza_sad_status
from wnioski w, analiza_prawna ap, analiza_operatora ao, analizy_wnioskow aw
where w.id = ap.id_wniosku
and ap.id_wniosku = ao.id_wniosku
and w.id = aw.id_wniosku
order by w.jezyk
limit 5;

----porownanie roznych dat znajdujacych sie w bazie dancyh
select w.id,
       w.jezyk,
       to_char(w.data_utworzenia, 'YYYY-MM-DD') as data_wnioksek_utw,
       to_char(aw.data_utworzenia, 'YYYY-MM-DD') as data_analiza_utw,
       to_char(aw.data_zakonczenia, 'YYYY-MM-DD') as data_zakonczenia,
       to_char(ap.data_odpowiedzi, 'YYYY-MM-DD') as data_odp_oper,
       date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) / 24.0 as czas_realziacji
from wnioski w, analizy_wnioskow aw, analiza_operatora ap
where w.id = aw.id_wniosku
and aw.id_wniosku = ap.id_wniosku
and to_char(aw.data_zakonczenia, 'YYYY-MM-DD') <> to_char(aw.data_utworzenia, 'YYYY-MM-DD')
and date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) / 24.0 > 0
order by jezyk;


---czas obslugi wnioskow w danym jezyku
with czas_realizacji as(
    select w.id as wniosek,
       w.jezyk as jezyk,
       date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) / 24.0 as dni_realziacji
    from wnioski w, analizy_wnioskow aw
    where w.id = aw.id_wniosku
    AND date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) / 24.0 > 0
    order by jezyk)
select jezyk,
       count(wniosek),
       AVG(dni_realziacji) as sredni_czas_realizacji_dni,
       AVG(dni_realziacji)*24.0 as sredni_czas_realizacji_godziny
from czas_realizacji
group by jezyk
order by sredni_czas_realizacji_dni DESC ;

------czas obslugi wnioskow w danym jezyku oraz w zaleznosci od typu podrozy (wartosc srednia)

select distinct typ_podrozy
from wnioski;

with czas_realizacji_typ_podrozy as(
    select w.id as wniosek,
       w.jezyk as jezyk,
       w.typ_podrozy as typ_podrozy,
       date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) / 24.0 as dni_realziacji
    from wnioski w, analizy_wnioskow aw
    where w.id = aw.id_wniosku
    AND date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) / 24.0 > 0
    AND w.typ_podrozy is not null
    order by jezyk)
select jezyk,
       typ_podrozy,
       count(wniosek),
       AVG(dni_realziacji) as sredni_czas_realizacji_dni,
       AVG(dni_realziacji)*24.0 as sredni_czas_realizacji_godziny
from czas_realizacji_typ_podrozy
group by jezyk, typ_podrozy
order by jezyk, sredni_czas_realizacji_dni DESC;

----dane do wykresu pudelkowy

with wykres_pudelkowy as(
    select w.id as wniosek,
       w.jezyk as jezyk,
       w.typ_podrozy as typ_podrozy,
       date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) / 24.0 as dni_realziacji
    from wnioski w, analizy_wnioskow aw
    where w.id = aw.id_wniosku
    AND date_part('hour', aw.data_zakonczenia - aw.data_utworzenia) / 24.0 > 0
    AND w.typ_podrozy is not null
    order by jezyk)
select jezyk,
       typ_podrozy,
       count(wniosek),
       percentile_disc(0.5) within group (order by dni_realziacji) as mediana_dni,
       percentile_disc(0.25) within group (order by dni_realziacji) as kwartyl_q1,
       percentile_disc(0.75) within group (order by dni_realziacji) as kwartyl_q3,
       max(dni_realziacji) as max_dni,
       min(dni_realziacji)  as min_dni
from wykres_pudelkowy
group by jezyk, typ_podrozy
order by jezyk, typ_podrozy DESC;