class Solution:
    def isValid(self, s: str) -> bool:
        order = {"{":"}", "[":"]", "(":")"}
        stack = []
        for c in s:
            if c in order:
                stack.append(c)
            elif stack:
                if order[stack[-1]] != c:
                    return False
                stack.pop()
            else:
                return False
        return True if not stack else False
            

