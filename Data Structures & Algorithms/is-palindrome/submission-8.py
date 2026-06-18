class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s) -1 
        s = s.lower()
        i = 0
        last = length
        while i < last:
            if not (s[last].isalnum()):
                last -= 1
            elif not (s[i].isalnum()):
                i += 1
            elif s[i] != s[last]:
                    return False
            else:
                last -=1
                i += 1
            
        return True
                
