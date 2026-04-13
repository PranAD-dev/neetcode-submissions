class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ans = 0
        while l < r:
            temp = abs(r-l)
            if heights[l] > heights[r]:
                temp*=heights[r]
                r-=1 
            else:
                temp*=heights[l]
                l+=1
            ans = max(temp, ans)
        
        return ans 