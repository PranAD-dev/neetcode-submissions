class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(numbers)):
            compl = target - numbers[i]
            if compl in hashmap:
                return [hashmap[compl]+1, i+1]
            else:
                hashmap[numbers[i]] = i
        
        