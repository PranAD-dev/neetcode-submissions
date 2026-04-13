class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        ans = []
        l = 0

        for r in range(len(nums)):

            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)

            if r-l+1 >= k:
                ans.append(nums[window[0]])
                if l in window:
                    window.remove(l)
                l+=1
        return ans    