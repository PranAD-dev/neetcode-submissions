class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set()
        for num in nums:
            if num in uniq:
                return True 
            else:
                uniq.add(num)
        return False