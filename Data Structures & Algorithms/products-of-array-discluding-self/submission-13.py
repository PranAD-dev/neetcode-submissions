class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        pref[0] = nums[0]
        current = 1
        for i in range(0,len(nums)):
            pref[i] = nums[i] * current 
            current = pref[i]
        suf = [0] * len(nums)
        suf[-1] = suf[-1]
        current = 1
        for i in range(len(nums)-1, -1,-1):
            suf[i] = nums[i] * current
            current = suf[i]
        ans = [0] * len(nums)
        ans[0] = suf[1]
        ans[-1] = pref[-2]

        for i in range(1,len(nums)-1):
            ans[i] = pref[i-1] * suf[i+1]
        
        return ans
