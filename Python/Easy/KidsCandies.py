# Problem: Kids With the Greatest Number of Candies (LeetCode #1431)
# Difficulty: Easy
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Finding the maximum number of candies among the kids
        max_candies = max(candies)
        
        # Creating the result list
        result = []
        
        # Iterating through each kid's candies
        for candy in candies:
            # Checking if the current kid can have the greatest number of candies
            result.append(candy + extraCandies >= max_candies)
        
        return result