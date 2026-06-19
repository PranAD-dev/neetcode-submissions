class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        ans = 0 

        while l < r:
            use = heights[r]
            if heights[l] < heights[r]:
                use = heights[l]

            val = use * (r - l)
            if val > ans:
                ans = val
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return ans
            
