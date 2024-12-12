# Problem: Can Place Flowers (LeetCode #605)
# Difficulty: Easy
# Link: https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # Initialising counter and availableSpots to plant
        i = 0
        availableSpots = 0
        
        # Checking if each 2 digit combination equates to 1, while adding extra criteria to
        # handle the first and last plots
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            # if the current plot is empty 
            # AND  
            # if this plot is the first OR if the previous plot is empty
            # AND
            # if this plot is the last OR if the next plot is empty
                availableSpots += 1
                i += 2
            else:
                i += 1
        
        return availableSpots >= n