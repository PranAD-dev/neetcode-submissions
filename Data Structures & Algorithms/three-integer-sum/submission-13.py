class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and (nums[i] == nums[i-1]):
                print(i)
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    output.add(tuple([nums[i], nums[j], nums[k]]))
                    j+=1
                    k-=1
                elif temp > 0:
                    k-=1
                else:
                    j+=1
        return list(output)
