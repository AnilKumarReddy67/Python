# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from
(
    select 
    lag(id) over (order by id) as prev_id,id,
    lead(id) over(order by id) as next_id,
    lag(num) over(order by id) as prev_num,num,
    lead(num) over (order by id) as next_num
    from logs
) sq
where prev_num=num and num=next_num and next_id-id=1 and id-prev_id=1;