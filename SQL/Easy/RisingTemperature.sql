-- Problem: Rising Temperature (LeetCode #197)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/rising-temperature

-- select ids
SELECT w1.id
-- from the weather table
FROM Weather w1
-- joined onto itself
JOIN Weather w2
-- where the first table is the current date and the second table is the previous date
ON w1.recordDate = w2.recordDate + INTERVAL 1 DAY
-- select only the ids where the current date has a greater temperature than the previous
WHERE w1.temperature > w2.temperature;
