# Write your MySQL query statement below

# company with name "RED"

# sale id with com_id name RED

# select sales_id not in previous table

select name
from SalesPerson
where sales_id not in (
    select sales_id
    from Orders
    where com_id in (
        select com_id
        from Company
        where name like "%RED%"
    )
)