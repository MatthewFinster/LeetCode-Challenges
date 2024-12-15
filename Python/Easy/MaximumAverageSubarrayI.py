# Problem: Maximum Average Subarray I (LeetCode #643)
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        maxSum = windowSum

        # This creates a sliding window where it adds the number at k (see i) in the list.
        # Because indexing starts at 0, this will mean that, for example, if k is 4, it will be the 5th number
        # It subtracts the number in the list that is k number of places before k (see i).
        # Between the current windowSum and the maxSum, the maxSum is updated
        # the loop continues until the length of the list is reached
        for i in range(k, len(nums)):
            windowSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, windowSum)
        
        # The average is returned
        return maxSum / k

        # Originally I coded a less efficient solution below:
        # i = 0
        # j = k
        # windows = []
    
        # while j <= len(nums):
        #    window = 0
        #    for num in nums[i:j]:
        #        window += num
        #    windows.append(window)
        #    i +=1
        #    j +=1

        # maxWindow = max(windows)
        # maxAverage = maxWindow / k

        # return maxAverage