class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        ans = 0
        arr = set()
        for r in range(n):
            
            while (s[r] in arr):
                arr.remove(s[l])
                l+=1
            arr.add(s[r])

            ans = max(ans,len(arr))
        
        return ans




