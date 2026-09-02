class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def func(temp: str) -> list[int]:
            rt = [0] * 26
            for c in temp:
                rt[ord(c) - ord('a')] +=1
            return rt
        
        compare = func(s1)
        for i in range(len(s2)-len(s1)+1):
            ag = func(s2[i:i+len(s1)])
            if compare == ag:
                return True
        
        return False

        