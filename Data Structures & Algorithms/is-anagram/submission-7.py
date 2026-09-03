class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def convert(word):
            output = [0] * 26
            
            for c in word:
                output[ord(c)-ord('a')] += 1
            return output
        return convert(s) == convert(t)