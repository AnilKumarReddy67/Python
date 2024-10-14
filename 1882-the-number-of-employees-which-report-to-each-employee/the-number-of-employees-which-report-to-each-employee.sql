# Write your MySQL query statement below
select e1.employee_id,e1.name,count(e2.reports_to) as reports_count,round(avg(e2.age*1.00),0) as average_age
from employees as e1
inner join employees e2 on e2.reports_to=e1.employee_id
group by e1.employee_id,e1.name
order by e1.employee_id;
