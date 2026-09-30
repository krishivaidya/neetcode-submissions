class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        i = 0 
        j = 0 
        maxlen = 0 

        for j in range(0, len(s)):

            if store.get(s[j], 0) == 0:
                store[s[j]] = 1
            else:
                while store.get(s[j], 0) != 0:
                    store[s[i]] -= 1
                    i += 1

                store[s[j]] = 1

            curlen = j - i + 1
            maxlen = max(curlen, maxlen)


        return maxlen
                



        