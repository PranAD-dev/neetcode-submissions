class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        left = 0
        max1 = 0
        for i in range(len(s)):
            while s[i] in uniq:
                uniq.remove(s[left])
                left+=1
            uniq.add(s[i])
            max1 = max(i-left+1, max1)
        return max1






