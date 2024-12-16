# Problem: Find the Highest Altitude (LeetCode #1732)
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Initialising variables for current altitude and max altitude
        alt = 0
        maxAlt = 0

        # For each list item
        for g in gain:
            alt += g #Add the integer onto the current altitude
            maxAlt = max(maxAlt, alt) # Check which is greater: the current altitude or the max altitude, update the max altitude with the response
        
        return maxAlt 
