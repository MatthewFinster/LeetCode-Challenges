<<<<<<< HEAD
-- Problem: Big Countries (LeetCode #595)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/big-countries/

SELECT name, population, area
FROM World
=======
-- Problem: Big Countries (LeetCode #595)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/big-countries/

SELECT name, population, area
FROM World
>>>>>>> 6384377afe47b08faddacc2d2cb4d3c636c4dd27
WHERE area >= 3000000 OR population >= 25000000