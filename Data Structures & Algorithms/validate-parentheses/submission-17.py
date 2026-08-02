class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s == "":
            return True
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == "}":
                if stack:
                    t = stack.pop()
                else: 
                    return False
                if t == "(" or t == "[":
                    return False 
            
            elif c == ")":
                if stack:
                    t = stack.pop()
                else: 
                    return False
                if t == "{" or t == "[":
                    return False 
            
            elif c == ']':
                if stack:
                    t = stack.pop()
                else: 
                    return False
                if t == "(" or t == "{":
                    return False 
        
        if stack:
            return False 
        
        
        return True
    


        