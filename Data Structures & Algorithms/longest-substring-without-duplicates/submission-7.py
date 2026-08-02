class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        l = 0
        r = 0
        maxl = 0
        while r < len(s):
            while s[r] in store:
                store.remove(s[l])
                l+= 1
            store.add(s[r])
            maxl = max(maxl, r - l + 1)
            r += 1
        

        return maxl
