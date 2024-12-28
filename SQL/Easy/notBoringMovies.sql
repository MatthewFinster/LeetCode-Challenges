-- Problem: Not Boring Movies (LeetCode #620)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/not-boring-movies

SELECT id, movie, description, rating
FROM Cinema
WHERE id % 2 != 0 AND description NOT LIKE '%boring%'
ORDER BY rating DESC;
