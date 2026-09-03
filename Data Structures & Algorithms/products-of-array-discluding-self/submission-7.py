class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        current = 1
        for num in nums:
            temp = num*current
            pref.append(temp)
            current = temp
        suff = [0] * len(nums)
        current = 1
        for i in range(len(nums)-1,-1,-1):
            suff[i] = nums[i] * current
            current = suff[i]
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(suff[1])
            elif i == len(nums) - 1:
                ans.append(pref[len(nums) - 2])
            else:
                ans.append(pref[i-1]*suff[i+1])
        return ans
        
