class Solution:
    def isValid(self, s: str) -> bool:
        hm = {'[' : ']', '{' : '}', '(' : ')'}
        st = []
        for i in s: 
            if i in hm.keys():
                st.append(i)
            elif i == ']' and st:
                if st[-1] == '[':
                    st.pop()
                else:
                    return False
            elif i == '}' and st:
                if st[-1] == '{':
                    st.pop()
                else:
                    return False
            elif i == ')' and st:
                if st[-1] == '(':
                    st.pop()
                else:
                    return False
            else:
                return False
        
        if st:
            return False 
        else:
            return True