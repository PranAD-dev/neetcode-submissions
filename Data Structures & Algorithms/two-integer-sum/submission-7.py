class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}

        for i in range(len(nums)):
            compliment = target-nums[i]
            if compliment in hash1:
                return [hash1[compliment], i]
            else:
                hash1[nums[i]] = i
        
        