class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        i = 0
        maxlength = 0
        j = 0

        for j in range(len(s)):
            store[s[j]] = store.get(s[j], 0) + 1
            mostfreq = max(store.values())
            length = j - i + 1
            replacements = length - mostfreq
            while replacements > k:
                store[s[i]] = store.get(s[i], 0) - 1
                i += 1
                length -= 1
                mostfreq = max(store.values())
                replacements = length - mostfreq

            maxlength = max(maxlength, length)


        return maxlength
        