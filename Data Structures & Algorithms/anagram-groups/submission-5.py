class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for word in strs:
            temp = [0] * 26
            for c in word:
                temp1 = ord('a') - ord(c)
                temp[temp1] += 1
            output[tuple(temp)].append(word)
        
        return list(output.values())
