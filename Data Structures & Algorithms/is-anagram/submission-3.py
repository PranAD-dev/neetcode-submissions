class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sn = [0] * 26
        tn = [0] * 26

        for char in s:
            sn[ord(char) - ord("a")] += 1
        for char in t:
            tn[ord(char) - ord("a")] += 1
        return sn == tn