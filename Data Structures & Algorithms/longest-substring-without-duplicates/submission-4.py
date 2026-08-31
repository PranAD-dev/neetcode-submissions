class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        check = set()
        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left+=1
            check.add(s[right])
            ans = max(right-left+1, ans)
        return ans


        