# Write your MySQL query statement below

# using limit in descending order

select customer_number
from 
(
    select customer_number, count(order_number) c
    from Orders
    group by customer_number
    order by c desc
    limit 1
) as T