# https://leetcode.com/problems/primary-department-for-each-employee/description/
# Write your MySQL query statement below
select employee_id, department_id from (
select employee_id, department_id, 
row_number() over (partition by employee_id order by primary_flag asc, department_id) rn from Employee)q
left join (select employee_id from Employee group by 1 having count(*) > 1
 and max(primary_flag) = 'N')q2 
using (employee_id)
where rn = 1 and q2.employee_id is null
