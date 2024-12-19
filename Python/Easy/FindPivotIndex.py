# Problem: Find Pivot Index (LeetCode #724)
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate the total sum of the array
        total = sum(nums)
        left_sum = 0
        
        # Iterate through the array with both index and value
        for i, num in enumerate(nums):
            # Check if the left sum equals the right sum
            # Right sum can be calculated as total - left_sum - num
            if left_sum == (total - left_sum - num):
                return i
            # Update the left sum to include the current element
            left_sum += num
        
        # If no pivot index is found, return -1
        return -1


        # My original solution works but is not the most efficient or optimised:
        
        # for i in range(len(nums)):
        #    leftIndex = 0
        #    rightIndex = 0
        #    for li in range(0, i):
        #        leftIndex += nums[li]
        #    for ri in range(i+1, len(nums)):
        #        rightIndex += nums[ri]
        #    if leftIndex == rightIndex:
        #        return i
        
        #return -1
