class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        i = 0

        for j in range(len(s2)):
            window[s2[j]] = window.get(s2[j], 0) + 1

            # window became too large
            if j - i + 1 > len(s1):
                window[s2[i]] -= 1

                if window[s2[i]] == 0:
                    del window[s2[i]]

                i += 1

            # window is exactly len(s1)
            if j - i + 1 == len(s1):
                if window == s1_count:
                    return True

        return False
        