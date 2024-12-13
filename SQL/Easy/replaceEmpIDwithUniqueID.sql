-- Problem: Replace Employee ID With The Unique Identifier (LeetCode #1378)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;
