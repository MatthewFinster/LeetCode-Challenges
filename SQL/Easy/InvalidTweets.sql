-- Problem: Invalid Tweets (LeetCode #1683)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/invalid-tweets

SELECT tweet_id
FROM Tweets
WHERE length(content) > 15
