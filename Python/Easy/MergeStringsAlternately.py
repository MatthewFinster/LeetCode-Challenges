# Problem: Merge Strings Alternately (LeetCode #1768)
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-strings-alternately/

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Initialising variables i and j to start at 0
        i, j = 0, 0
        # Initialising the list called merged
        merged = []

        # Merging characters alternately 
        while i < len(word1) or j < len(word2):
            if i < len(word1): 
                merged.append(word1[i])
                i += 1
            if j < len(word2):
                merged.append(word2[j])
                j += 1
        
        # Joining the list onto an empty string and returning it
        return ''.join(merged)
