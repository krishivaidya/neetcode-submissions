class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxcount = 0
        st = set()
        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            maxcount = max(maxcount, r - l + 1)
        return maxcount



        