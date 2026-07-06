class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n2 = len(s2)
        n1 = len(s1)
        if n1 > n2:
            return False
        def convert(s: str) -> list[int]:
            output = [0] * 26
            for char in s:
                pos = ord(char) - ord('a')
                output[pos] += 1
            return output
        comp = convert(s1)
        
        temp = convert(s2[:n1])

        if comp == temp:
            return True
        
        for i in range(n1,n2):
            temp[ord(s2[i]) - ord('a')] += 1
            temp[ord(s2[i-n1]) - (ord('a'))] -= 1

            if comp == temp:
                return True

        return False
            




