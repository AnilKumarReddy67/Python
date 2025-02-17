# Write your MySQL query statement below
select s.user_id,round(avg(if(c.action='confirmed',1,0)),2) as confirmation_rate
from signups as s left join confirmations as c on c.user_id=s.user_id
group by s.user_id;