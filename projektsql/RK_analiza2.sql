select
abc.jezyk,
sum(abc.liczba_wnioskow),
case when abc.rating < 1 then '1. rating <1'
    when abc.rating >= 1 and abc.rating < 50 then '2. rating 1-49'
    when abc.rating >= 50 then '3. rating >50' else null end
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

case when abc.rating < 1 then '1. rating <1'
    when abc.rating >= 1 and abc.rating < 50 then '2. rating 1-49'
    when abc.rating >= 50 then '3. rating >50' else null end,
abc.jezyk
order by sum(abc.liczba_wnioskow) desc
;
select
*
from m_kampanie mk
join m_email me on mk.id = me.id_kampanii
where mk.id = '802'