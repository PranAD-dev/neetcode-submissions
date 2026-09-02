class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left = 0 
        right = len(heights) - 1
        while left < right:
            if heights[right] > heights[left]:
                temp = heights[left] * (right-left)
                left+=1
            else:
                temp = heights[right] * (right - left) 
                right-=1
            
            ans = max(temp, ans)
        return ans
