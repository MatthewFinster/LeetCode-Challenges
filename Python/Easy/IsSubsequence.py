# Problem: Is Subsequence (LeetCode #392)
# Difficulty: Easy
# Link: https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Two pointers
        j = 0
        i = 0

        # For efficinecy, the while loop stops either if the subsequence has been found,
        # or if it finishes searching all the way through t
        while i < len(s) and j < len(t):
            # if the index matches, we look for the next letter in s
            if s[i] == t[j]:
                i += 1
            # we increase the index of t, regardless
            j += 1
        
        # Its true if the length of s is the same number as i,
        # as all letters will have been counted within t
        return i == len(s) 
