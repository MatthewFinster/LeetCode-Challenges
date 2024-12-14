-- Problem: Product Sales Analysis I (LeetCode #1068)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/product-sales-analysis-i

SELECT p.product_name, s.year, s.price
FROM Sales AS s INNER JOIN Product AS p
ON s.product_id = p.product_id;
