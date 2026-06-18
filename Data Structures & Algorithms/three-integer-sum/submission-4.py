class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n - 1
            
            while j < k:                    
                val = nums[i] + nums[j] + nums[k]
                
                if val == 0:
                    output.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                    j+=1
                    k-=1
                elif val < 0:
                    j+=1
                else:
                    k-=1
                    
        return list(output)
            


        

            
        