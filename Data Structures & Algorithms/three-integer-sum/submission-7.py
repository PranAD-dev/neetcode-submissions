class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                f = nums[i]
                s = nums[j]
                t = nums[k]
                total = f + s + t
                if total == 0:
                    output.add(tuple([f,s,t]))
                    j += 1
                    k -= 1
                elif total < 0: 
                    j += 1
                else:
                    k -= 1
        return list(output)

           

        

            
        