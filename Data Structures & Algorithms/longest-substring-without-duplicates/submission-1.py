class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        counts = set()
        for right in range(len(s)): 
            while s[right] in counts:
                counts.remove(s[left])
                left+=1
            
            counts.add(s[right]) 
            ans = max(right-left+1,ans)
        return ans