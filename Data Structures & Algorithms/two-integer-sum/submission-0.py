class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in indexes:
                return [indexes[compliment], i]
            else:
                indexes[nums[i]] = i
