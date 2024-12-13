# Problem: Reverse Vowels of a String (LeetCode #345)
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        # Initalising a set of vowels
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        # Strings are immutable so converting the string to a list
        s = list(s)
        # Initialising character/counter 1 and character/counter 2
        c1 = 0
        c2 = len(s) - 1

        # While loop that meets at halfway in the list
        while c1 < c2:
            if s[c1] not in vowels:
                c1 += 1
            elif s[c2] not in vowels:
                c2 -= 1
            else:
                s[c1], s[c2] = s[c2], s[c1]
                c1 += 1
                c2 -= 1

        # Converting the list back to string
        return ''.join(s)
                 
