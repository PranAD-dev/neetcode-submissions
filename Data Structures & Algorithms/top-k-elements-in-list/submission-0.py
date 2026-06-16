class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans = []
        for i in range(k):
            temp = max(freq,key=freq.get)
            ans.append(temp)
            freq.pop(temp)
        return ans
