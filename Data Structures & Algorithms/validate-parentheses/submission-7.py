class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")" : "(", "}" : "{", "]" : "["}
        
        for c in range(len(s)):
            if s[c] in match:
                if not stack or stack[-1] != match[s[c]]:
                    return False 
                else:
                    stack.pop()
            
            else:
                stack.append(s[c])
        
        if not stack:
            return True
        else:
            return False


        