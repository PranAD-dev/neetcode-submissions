class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert_to_list(word):
            output = [0] * 26
            for c in word:
                output[ord(c)-ord("a")] += 1
            return output
        
        hash1 = defaultdict(list)

        for word in strs:
            hash1[tuple(convert_to_list(word))].append(word)
        
        return list(hash1.values())
