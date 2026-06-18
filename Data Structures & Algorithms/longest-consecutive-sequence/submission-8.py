class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            curr = num
            temp = 0
            if len(nums) >= 1:
                temp = 1
            while curr + 1 in nums:
                temp+=1
                curr += 1
            if temp > ans:
                ans = temp
            
        
        return ans