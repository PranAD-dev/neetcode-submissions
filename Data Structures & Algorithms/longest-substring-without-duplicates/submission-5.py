class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cont_set = set()
        left = ans = 0
        for right in range(len(s)):
            while s[right] in cont_set:
                cont_set.remove(s[left])
                left+=1
            cont_set.add(s[right])
            ans = max(right-left+1, ans)
        return ans