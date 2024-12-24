# Problem: Find the Difference of Two Arrays (LeetCode #2215)
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Converting both lists to sets to remove duplicates and allow set operations
        set1 = set(nums1)
        set2 = set(nums2)
        
        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)
        
        return [diff1, diff2] 
