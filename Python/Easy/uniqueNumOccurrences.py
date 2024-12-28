# Problem: Counting UNique Number of Occurrences (LeetCode #1207)
# Difficulty: Easy
# Link: https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for item in arr:
            counts[item] = counts.get(item, 0) + 1

        if len(set(counts.values())) != len(counts.values()):
            return False

        return True