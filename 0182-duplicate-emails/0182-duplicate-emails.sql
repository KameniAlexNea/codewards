# Write your MySQL query statement below
# select distinct p1.email as email
# from Person as p1
# join Person as p2
# on p1.email = p2.email and p1.id != p2.id;

# Using group by
SELECT DISTINCT email AS Email  FROM Person
WHERE email IN
(SELECT CASE WHEN COUNT(id)>1 THEN email
END
FROM Person
GROUP BY email);