class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check 1: do they have the same characters?
        # Check 2: do they have the same number of characters?
        if len(s) != len(t):
            return False

        countOne = [0]*26
        countTwo = [0]*26

        for i in range(len(s)):
            countOne[ord(s[i])-ord('a')] +=1
            countTwo[ord(t[i])-ord('a')] +=1

        return countOne == countTwo

