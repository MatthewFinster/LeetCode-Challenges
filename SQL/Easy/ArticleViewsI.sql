-- Problem: Article Views I (LeetCode #1148)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/article-views-i/

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;