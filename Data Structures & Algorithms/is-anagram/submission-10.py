class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}

        for i in s:
            store[i] = store.get(i,0) + 1

        for j in t:
            if store.get(j,0) == 0:
                return False
            store[j] = store[j] - 1

        if max(store.values())> 0:
            return False
        else:
            return True 
        
        