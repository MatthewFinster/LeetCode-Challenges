-- Problem: Employee Bonus (LeetCode #577)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/employee-bonus

 SELECT e.name, b.bonus 
 FROM Employee e 
 LEFT JOIN Bonus b
 ON e.empID = b.empID
 WHERE b.bonus < 1000 OR b.bonus IS NULL;
