class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() 
        length = len(s) -1 
        left = 0 
        right = length 
        while left < right:
            if not (s[left].isalnum()):
                left+=1
            elif not (s[right].isalnum()):
                right-=1
            else:

                if (s[left] != s[right]):
                    return False
                else:
                    left +=1
                    right -=1
        return True
                

