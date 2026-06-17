class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output = output + str(len(word)) + "{" + word
        return output
    def decode(self, s: str) -> List[str]:
        print(s)
        output = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "{":
                j+=1
            length = int(s[i:j])
            i = j+1
            word = s[i:i+length]
            output.append(word)
            i += length
        return output

