class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        n = len(nums)
        for i in range(n):
            hashmap = {}
            for j in range(n):
                if i==j:
                    continue
                
                compl = 0 - nums[i] - nums[j]
                if compl in hashmap:
                    output.add(tuple(sorted([nums[i],nums[j],compl])))
                else:
                    hashmap[nums[j]] = j
        return list(output)



            
        