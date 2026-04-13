class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1 
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    temp_arr = [nums[i],nums[left],nums[right]]
                    if temp_arr not in ans:
                        ans.append(temp_arr)
                    right-=1
                    left+=1
                elif temp > 0:
                    right -= 1
                else:
                    left+=1
        return ans

    
