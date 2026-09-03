class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1 = Counter(nums)
        output = []
        for i in range(k):
            key = max(hash1, key=hash1.get)
            output.append(key)
            del hash1[key]
        return output