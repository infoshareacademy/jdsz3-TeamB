-- Analiza - gdzie trafia najwięcej leadow
select
    w.jezyk,
    count(w.id) as liczba_wnioskow,
    count(ml.id_wniosku) as liczba_leadow,
    count(ml.id) as liczba_leadow_id,
    round((count(ml.id_wniosku)  /  count(w.id)::numeric * 100),2) as procent
from wnioski w
left join m_lead ml on ml.id_wniosku = w.id
group by w.jezyk
order by 4 desc
;


-- Utworzenie tabeli ze statystykami kampanii w airhelp
create table m_kampanie_statystyki as
(
with statystyki as
(
select
    mk.id as id_kampanii,
    mk.typ_kampanii,
    mk.data_kampanii,
    mk.status,
    me.id as id_email,
    case when me.ile_otwarto > 0 then 1 else 0 end as ile_otwarto,
    case when me.ile_kliknieto > 0 then 1 else 0 end as ile_kliknieto
from m_kampanie mk
join m_email me on mk.id = me.id_kampanii
where mk.typ_kampanii = 'kampania glowna'
)

select
    id_kampanii,
    typ_kampanii,
    data_kampanii,
    status,
    count(id_email) as ile_wyslano,
    sum(ile_otwarto) as ile_otwarto,
    sum(ile_kliknieto) as ile_kliknieto,
    round ((sum(ile_otwarto) / count(id_email)::numeric),3)   as open_rate,
    round ((sum(ile_kliknieto) / count(id_email)::numeric),3)   as ctr
from statystyki
group by
    id_kampanii,
    typ_kampanii,
    data_kampanii,
    status
);


-- Zapytania pomocnicze w celu stworzenia grup dla wskaźników opisujących kampanie

    select
        percentile_disc(0.25) within group (order by ile_wyslano) as q1_ile_wyslano,
        percentile_disc(0.5) within group (order by ile_wyslano) as mediana_ile_wyslano,
        percentile_disc(0.75) within group (order by ile_wyslano) as q3_ile_wyslano,
        avg(ile_wyslano)
    from m_kampanie_statystyki;

    -- powstaną dwie grupy dla określenia wielkości kampanii na podstawie ilości wysłanych emaili:
        -- mała do 350 emaili
        -- duża powyżej 350 emaili


    select
        percentile_disc(0.25) within group (order by open_rate) as q1,
        percentile_disc(0.5) within group (order by open_rate) as mediana,
        percentile_disc(0.75) within group (order by open_rate) as q3,
        avg(open_rate)
    from m_kampanie_statystyki;

    -- powstaną trzy grupy dla określenia open_rate kampanii na podstawie ilości otwartych emaili w stosunku do wysłanych emaili:
        -- spam - open_rate = 0
        -- dobra reklama - 0 < open_rate < 0,8
        -- intrygująca reklama - open_rate >= 0,8

    select
        percentile_disc(0.25) within group (order by ctr) as q1,
        percentile_disc(0.5) within group (order by ctr) as mediana,
        percentile_disc(0.75) within group (order by ctr) as q3,
        avg(ctr)
    from m_kampanie_statystyki;

    -- powstaną trzy grupy dla określenia ctr kampanii na podstawie ilości klikniętych linków w stosunku do wysłanych emaili:
        -- spam - open_rate = 0
        -- dobra reklama - 0 < open_rate < 0,66
        -- intrygująca reklama - open_rate >= 0,66


-- Dodanie kolumn opisowych

alter table m_kampanie_statystyki add wielkosc_kampanii varchar(50);
alter table m_kampanie_statystyki add open_rate_opis varchar(50);
alter table m_kampanie_statystyki add ctr_opis varchar(50);

update m_kampanie_statystyki set wielkosc_kampanii = 'mała'
where ile_wyslano < 350;
update m_kampanie_statystyki set wielkosc_kampanii = 'duża'
where ile_wyslano >= 350;


update m_kampanie_statystyki set open_rate_opis = 'spam'
where open_rate = 0;
update m_kampanie_statystyki set open_rate_opis = 'dobra reklama'
where open_rate > 0 and open_rate < 0.8;
update m_kampanie_statystyki set open_rate_opis = 'intrygująca reklama'
where open_rate >= 0.8;


update m_kampanie_statystyki set ctr_opis = 'spam'
where ctr = 0;
update m_kampanie_statystyki set ctr_opis = 'dobra reklama'
where ctr > 0 and ctr < 0.66;
update m_kampanie_statystyki set ctr_opis = 'intrygująca reklama'
where ctr >= 0.66;



select * from m_kampanie_statystyki
where ctr >= 0.66;

--Analiza: jezyk wniosku a przypisanie do potencjalnej kampanii

-- open rate

select
jezyk,
sum(spam) as spam,
sum(dobra_reklama) as dobra_reklama,
sum(intrygujaca_reklama) as intrygujaca_reklama,
100.0*sum(spam)/ (sum(spam)+sum(dobra_reklama)+sum(intrygujaca_reklama)) as procent_spam,
100.0*sum(intrygujaca_reklama)/ (sum(spam)+sum(dobra_reklama)+sum(intrygujaca_reklama)) as procent_intrygujaca_reklama
from
(
select
jezyk,
open_rate_opis,
case when open_rate_opis = 'spam' then sum(liczba_wnioskow) else 0 end as spam,
case when open_rate_opis = 'dobra reklama' then sum(liczba_wnioskow) else 0 end as dobra_reklama,
case when open_rate_opis = 'intrygująca reklama' then sum(liczba_wnioskow) else 0 end as intrygujaca_reklama
from
(
select
    w.jezyk,
    count (w.id) as liczba_wnioskow,
    mks.open_rate_opis
from wnioski w
join m_lead ml on ml.id_wniosku = w.id
join m_lead_kampania mlk on ml.id = mlk.id_lead
join m_kampanie_statystyki mks on mlk.id_kampania = mks.id_kampanii
group by
    w.jezyk,
    mks.open_rate_opis
) abc
group by
jezyk,
open_rate_opis
) xyz
group by
jezyk
order by 6 desc
;

-- ctr
select
jezyk,
sum(spam) as spam,
sum(dobra_reklama) as dobra_reklama,
sum(intrygujaca_reklama) as intrygujaca_reklama,
100.0*sum(spam)/ (sum(spam)+sum(dobra_reklama)+sum(intrygujaca_reklama)) as procent_spam,
100.0*sum(intrygujaca_reklama)/ (sum(spam)+sum(dobra_reklama)+sum(intrygujaca_reklama)) as procent_intrygujaca_reklama
from
(
select
jezyk,
ctr_opis,
case when ctr_opis = 'spam' then sum(liczba_wnioskow) else 0 end as spam,
case when ctr_opis = 'dobra reklama' then sum(liczba_wnioskow) else 0 end as dobra_reklama,
case when ctr_opis = 'intrygująca reklama' then sum(liczba_wnioskow) else 0 end as intrygujaca_reklama
from
(
select
    w.jezyk,
    count (w.id) as liczba_wnioskow,
    mks.ctr_opis
from wnioski w
join m_lead ml on ml.id_wniosku = w.id
join m_lead_kampania mlk on ml.id = mlk.id_lead
join m_kampanie_statystyki mks on mlk.id_kampania = mks.id_kampanii
group by
    w.jezyk,
    mks.ctr_opis
) abc
group by
jezyk,
ctr_opis
) xyz
group by
jezyk
order by 6 desc
;

-- Analiza - w jakim stopniu partner wybierając czy przypisać lead dla danego wniosku zwraca uwagę na język
-

-- dopracowac
select
    w.jezyk,
    md.partner,
    count(w.id) as liczba_wnioskow,
    count(ml.id_wniosku) as liczba_leadow,
    count(ml.id) as liczba_leadow_id,
    round((count(ml.id_wniosku)  /  count(w.id)::numeric * 100),2) as procent
from wnioski w
left join m_lead ml on ml.id_wniosku = w.id
left join m_dane_od_partnerow md on md.id = ml.id
group by
    w.jezyk,
    md.partner
order by 5 desc
;

-- Analiza - w jakim stopniu partner wybierając kampanię dla danego wniosku zwraca uwagę na język









-- eksploracja bazy

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
