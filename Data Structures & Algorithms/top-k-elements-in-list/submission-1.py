class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        has = Counter(nums)
        num = Counter.most_common(has)
        for i in range(k):
            ans.append(num[i][0])
        return ans