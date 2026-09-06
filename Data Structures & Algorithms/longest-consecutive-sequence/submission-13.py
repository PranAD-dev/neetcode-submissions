class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        
        nums = set(nums)
        ans = 1
        for num in nums: 
            if (num-1) not in nums:
                temp = 1
                curr = num
                while (curr+ 1) in nums:
                    temp+=1
                    curr+=1
                
                ans = max(ans, temp)
        
        return ans
                    