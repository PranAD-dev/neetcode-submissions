class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s) -1 
        t = s.lower()
        i = 0
        last = length
        while i < last:
            if not (t[last].isalnum()):
                last -= 1
            elif not (t[i].isalnum()):
                i += 1
            elif t[i] != t[last]:
                    return False
            else:
                last -=1
                i += 1
            
        return True
                
