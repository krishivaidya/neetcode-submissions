class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        check = set()
        l = 0
        r = 0
        while r < len(s):
            while s[r] in check:
                check.remove(s[l])
                l += 1
                
            maxlength = max(maxlength, (r - l)+ 1)
            check.add(s[r])
            r += 1
        return maxlength


        