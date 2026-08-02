class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        store = {")" : "(", "}": "{", "]": "["}

        for i in s:
            if i in store and st:
                if store[i] != st.pop():
                    return False
            else:
                st.append(i)

        if st:
            return False

        return True        