class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        check = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in check:
                check.add(s[r])
                maxlength = max(maxlength, (r - l)+ 1)
                r += 1

            else:
                while s[r] in check:
                    check.remove(s[l])
                    l += 1
                
            
           
           
        return maxlength


        