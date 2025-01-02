-- Problem: Average Selling Price (LeetCode #1251)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/average-selling-price/

SELECT p.product_id, ROUND(IFNULL(SUM(p.price * u.units) / NULLIF(SUM(u.units), 0), 0),2) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
