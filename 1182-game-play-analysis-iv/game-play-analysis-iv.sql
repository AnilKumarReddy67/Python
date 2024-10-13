# Write your MySQL query statement below

#using common table expression

with temp as
(select player_id,min(event_date) as first_login
from Activity
group by player_id
)

select round(sum(datediff(a.event_date,t.first_login)=1)/count(distinct a.player_id),2)
as fraction
from Activity as a
join temp as t on t.player_id=a.player_id;
