class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s) -1 
        i = 0
        last = length
        while i < last:
            if not (s[last].isalnum()):
                last -= 1
            elif not (s[i].isalnum()):
                i += 1
            elif s.lower()[i] != s.lower()[last]:
                    return False
            else:
                last -=1
                i += 1
            
        return True
                
