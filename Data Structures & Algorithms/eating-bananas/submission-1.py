class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            return sum(math.ceil(pile / k) for pile in piles)

        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if hours(mid) <= h:      
                ans = mid
                right = mid - 1
            else:                   
                left = mid + 1

        return ans