class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        counter = 1 
        for num in nums:
            temp = num * counter
            pref.append(temp)
            counter = temp
        counter = 1
        suff = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            temp = counter * nums[i]
            suff[i] = temp
            counter = temp
        output = [0] * len(nums)
        back = 1
        for i in range(len(nums)):
            if i == 0:
                output[i] = suff[i+1]
            elif i == len(nums) - 1:
                output[i] = pref[i-1]
            else:
                output[i] = pref[i-1] * suff[i+1]
        return output
            
            
