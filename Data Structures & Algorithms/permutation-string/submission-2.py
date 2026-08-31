class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def func(list1):
            ort = [0] * 26
            for c in list1:
                ort[ord(c)-ord('a')] +=1
            return ort
        compare = func(s1)

        for left in range(len(s2)-len(s1)+1):
            temp = s2[left:left+len(s1)]
            temp = func(temp)
            if temp == compare:
                return True
        return False
        
       
