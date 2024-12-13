# Problem: Move Zeroes (LeetCode #283) 
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index1 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index1] = nums[i]
                index1 += 1

        for i in range(index1, len(nums)):
            nums[i] = 0