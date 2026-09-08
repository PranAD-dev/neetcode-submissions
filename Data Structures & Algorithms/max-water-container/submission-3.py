class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        ans = 0

        while left < right:
            if heights[left] > heights[right]:
                curr = heights[right] * (right - left)
                ans = max(ans, curr)
                right-=1
            else:
                curr = heights[left] * (right - left)
                ans = max(ans, curr)
                left+=1
        
        return ans

   