# Write your MySQL query statement below

with ActivityRank as (
    select player_id, event_date first_login, (
        ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date asc)
    ) AS r
    from Activity
)
select player_id, first_login
from ActivityRank
where r = 1