class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n
        for i in range(n):
            if i == 0:
                leftmax[i] = 0
                continue
            if (height[i-1] >= leftmax[i-1]):
                leftmax[i] = height[i-1]
            else:
                leftmax[i] = leftmax[i-1]
 
        for i in range(n-1, -1, -1):
            if i == n - 1:
                rightmax[i] = 0
                continue
            if (height[i + 1] >= rightmax[i + 1]):
                rightmax[i] = height[i+1]
            else:
                rightmax[i] = rightmax[i+1]
        total = 0
        for i in range(n):
            ans = min(leftmax[i],rightmax[i]) - height[i]
            if ans <=0:
                ans = 0
            total+=ans

        return total

        



        
            
        
    
            


            

