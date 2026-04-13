class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        perceset = set()
        for num in nums:
            if num in perceset:
                return True
            else:
                perceset.add(num)
        return False