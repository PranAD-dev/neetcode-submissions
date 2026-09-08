class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def ord1(word):
            temp = [0] * 26
            for c in word:
                temp[ord(c)-ord('a')] += 1
            return temp
        return ord1(s) == ord1(t)
 