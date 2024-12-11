-- Problem: Recyclable and Low Fat Products (LeetCode #1757)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/recyclable-and-low-fat-products/

-- This problem asks me to find the IDs of products that are both low fat and recycable
-- To solve the problem, I simply need to use SELECT statements to get the IDs WHERE low_fats = 'Y' AND recyclable = 'Y' 

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
