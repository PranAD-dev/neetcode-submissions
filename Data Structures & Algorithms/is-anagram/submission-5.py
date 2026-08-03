class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa = [0] * 26
        ta = [0] * 26

        for c in s:
            index = ord(c) - ord('a')
            sa[index] +=1 
        for c in t:
            index = ord(c) - ord('a')
            ta[index] +=1 
        return sa == ta
            
        