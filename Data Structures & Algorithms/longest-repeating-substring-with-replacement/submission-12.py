class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = {}
        ans = left = 0
        for right in range(len(s)):
                curr[s[right]] = curr.get(s[right], 0) + 1
                while (sum(curr.values()) - curr[max(curr, key=curr.get)]) > k:
                    print(sum(curr.values()) - curr[max(curr, key=curr.get)])
                    curr[s[left]] -= 1
                    left+=1
                ans = max(right-left+1, ans)
        return ans