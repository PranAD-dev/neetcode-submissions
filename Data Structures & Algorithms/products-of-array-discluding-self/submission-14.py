class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [0] * n 
        suffix = [0] * n 
        output = [0] * n

        # prefix first
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        # suffix second 
        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        # output third
        output[0] = suffix[1]
        output[-1] = prefix[n-2]

        for i in range(1, n-1):
            output[i] = prefix[i-1] * suffix[i+1]
        
        return(output)



        
        