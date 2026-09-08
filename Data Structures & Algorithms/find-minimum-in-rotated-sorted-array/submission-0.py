class Solution:
    def findMin(self, nums: List[int]) -> int:
        min1 = math.inf

        for num in nums:
            if num < min1:
                min1 = num
        
        return min1