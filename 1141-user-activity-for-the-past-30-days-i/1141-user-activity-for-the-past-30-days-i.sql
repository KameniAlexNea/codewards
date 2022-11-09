# Write your MySQL query statement below
select activity_date day, count(distinct user_id) active_users
from Activity
where 0 <= DATEDIFF("2019-07-27", activity_date) and DATEDIFF("2019-07-27", activity_date) < 30
group by activity_date;