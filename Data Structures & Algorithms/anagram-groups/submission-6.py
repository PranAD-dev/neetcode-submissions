class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                temp[index]+=1
            temp = tuple(temp)
            answer[temp].append(s)
        rans = []
        for i,(l,j) in enumerate(answer.items()):
            temp = []
            for k in j:
                temp.append(k)
            rans.append(temp)
            
        return rans
