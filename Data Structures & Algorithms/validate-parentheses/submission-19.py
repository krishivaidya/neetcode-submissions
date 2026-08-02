class Solution:
    def isValid(self, s: str) -> bool:
        store = {")" : "(", "]" : "[","}" : "{"}
        stack = []

        for i in s: 
            if stack and i in store:
                if store[i] != stack.pop():
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True
                
                

        