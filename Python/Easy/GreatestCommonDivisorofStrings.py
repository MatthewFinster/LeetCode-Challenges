# Problem: Greatest Common Divisor of Strings (LeetCode #1071)
# Difficulty: Easy
# Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
 
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # Ensuring str1 is a repetition of str2, if not the
        # program returns an empty string
        if str1 + str2 != str2 + str1:
            return ""

        # After satisfying the previous condition, 
        # finding the GCD and using this to return 
        # the part of str2 that repeats in str1
        gcd_length = math.gcd(len(str1), len(str2))
        return str1[:gcd_length]