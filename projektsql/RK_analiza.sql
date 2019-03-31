-- kampanie - które sa ciekawe / spamowe
create table m_kampanie_statystyki as
(
select
mk.id, mk.typ_kampanii, mk.data_kampanii, mk.status
, count(me.id) as liczba_mail_popularnosc
, sum(me.ile_otwarto) as ile_otwarto
, sum(me.ile_kliknieto) as ile_kliknieto
, case when sum(me.ile_otwarto) > 0 then
            round ((100.0 * sum(me.ile_kliknieto)/ sum(me.ile_otwarto)),2)
      else 0 end as Rating
from m_kampanie mk
join m_email me on mk.id = me.id_kampanii
--where me.id_kampanii = '844'
--where mk.typ_kampanii = 'kampania glowna'
group by
mk.id, mk.typ_kampanii, mk.data_kampanii, mk.status
-- having sum(me.ile_otwarto) < sum(me.ile_kliknieto) -- te warunek pokazuje ze raczej wiecej sie otwiera niz klika
--order by sum(me.ile_otwarto) desc
--order by count(me.id) desc
)
;


select
abc.jezyk,
sum(abc.liczba_wnioskow),
case when abc.rating < 1 then '1. rating <1'
     when abc.rating >= 1 and abc.rating < 20 then '2. rating 1-19'
     when abc.rating >= 20 and abc.rating < 30 then '3. rating 20-29'
     when abc.rating >= 30 and abc.rating < 40 then '4. rating 30-39'
     when abc.rating >= 40 and abc.rating < 50 then '5. rating 40-49'
     when abc.rating >= 50 then '6. rating >50' end
     as Atrakcyjnosc_kampanii
from
(
select
count (w.id) as liczba_wnioskow
 , w.jezyk
 ,mks.id
 ,mks.typ_kampanii
 ,mks.liczba_mail_popularnosc
 ,mks.rating

--, ntile(10) over (order by mks.liczba_mail_popularnosc)
from wnioski w
join m_lead ml on ml.id_wniosku = w.id
join m_lead_kampania mlk on ml.id = mlk.id_lead
join m_kampanie_statystyki mks on mlk.id_kampania = mks.id
where typ_kampanii = 'kampania glowna'
--and w.id = '2096459'
group by
 w.jezyk
 ,mks.id
 ,mks.typ_kampanii
 ,mks.liczba_mail_popularnosc
 ,mks.rating
) abc
group by
abc.jezyk,
case when abc.rating < 1 then '1. rating <1'
    when abc.rating >= 1 and abc.rating < 20 then '2. rating 1-19'
     when abc.rating >= 20 and abc.rating < 30 then '3. rating 20-29'
     when abc.rating >= 30 and abc.rating < 40 then '4. rating 30-39'
     when abc.rating >= 40 and abc.rating < 50 then '5. rating 40-49'
    when abc.rating >= 50 then '6. rating >50' end
--order by sum(abc.liczba_wnioskow) desc
--where abc.jezyk = 'pl'
;
--

-- gdzie trafia najwięcej leadow
select w.jezyk,
count(w.id) as liczba_wnioskow,
count(ml.id_wniosku) as liczba_leadow,
count(ml.id) as liczba_leadow_id,
round((count(ml.id_wniosku)  /  count(w.id)::numeric * 100),2) as procent
from wnioski w
left join m_lead ml on ml.id_wniosku = w.id
group by w.jezyk
order by 4 desc
;





-- 146 065
select count (distinct id) from m_lead;
-- 46 894
select count (distinct id_wniosku) from m_lead;
-- 99 171 -- tyle leadow nie ma wniosku przypisanego
select id_wniosku, count (distinct id)  from m_lead
group by id_wniosku
having count (distinct id) > 1;

-- lead moze być 1 lub brak
select w.jezyk, w.id, count(ml.id_wniosku) as liczba_leadow
from wnioski w
left join m_lead ml on ml.id_wniosku = w.id
group by w.jezyk, w.id
having count(ml.id_wniosku)  > 1
;

-- 1063
select count (distinct id_kampania) from m_lead_kampania;

-- 144 113
select count (distinct id_lead) from m_lead_kampania;

-- 1063
select count (distinct id_kampanii) from m_email;

-- 1063
select count (distinct id) from m_kampanie;

select distinct status from m_kampanie;
--oczekuje
--wyslane
--nowa




select w.id,  w.jezyk,  avg (extract (day from ml.data_wysylki - w.data_utworzenia)) as liczba_dni
from wnioski w
left join m_lead ml on ml.id_wniosku = w.id
where jezyk = 'ro'
group by w.jezyk, w.id
;



-- data wysyłki a data utworzenia wniosku -- dla ponizszego przykladu wszytskie 4 kampanie
select *
from wnioski w
left join m_lead ml on ml.id_wniosku = w.id
left join m_dane_od_partnerow md on md.id = ml.id
left join m_lead_kampania mlk on ml.id = mlk.id_lead
left join m_kampanie mk on mlk.id_kampania = mk.id
--left join m_email me on mk.id = me.id_kampanii
where --ml.data_wysylki < mk.data_kampanii
w.id = '2096459'  --and id_kampanii = '844'
;

-- to na pozniej
select * from m_dane_od_partnerow;