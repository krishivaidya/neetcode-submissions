class Solution:
    def isValid(self, s: str) -> bool:
        store = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                store.append(s[i])
            
            elif s[i] == '}':
                if not store or store[-1] != '{':
                    return False 
                else:
                    store.pop()
            
            elif s[i] == ')':
                if not store or store[-1] != '(':
                    return False 
                else:
                    store.pop()
            

            elif s[i] == ']':
                if not store or store[-1] != '[':
                    return False 
                else:
                    store.pop()
        
        if store:
            return False 
        
        return True
                
        