class Solution:
    def isValid(self, s: str) -> bool:
        check= {")" : "(", "}" : "{" , "]" : "["}
        stack = []
        for i in s:
            if i in check:
                if stack and check[i] != stack[-1] :
                    return False
                elif not stack:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        
        if not stack:
            return True
        else: 
            return False

        