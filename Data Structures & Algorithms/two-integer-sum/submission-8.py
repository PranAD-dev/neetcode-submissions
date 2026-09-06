class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}
        n = len(nums)
        for i in range(n):
            comp = target - nums[i]        
            if comp in hash1:
                return [hash1[comp], i]
            else:
                hash1[nums[i]] = i
        
        
