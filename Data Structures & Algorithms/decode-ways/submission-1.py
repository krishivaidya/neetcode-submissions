class Solution:
    def numDecodings(self, s: str) -> int:
        isvalid = {str(i) : chr(ord("A") + i - 1) for i in range(1, 27)}
        memo = {}
        def back(i):
            total = 0
            if i >= len(s):
                return 1
            if i in memo:
                return memo[i]
            for j in range(i, len(s)):
                if s[i:j+1] in isvalid:
                    x = back(j + 1)
                    if x != 0:
                        total += x
            memo[i] = total
            return memo[i]
        
        return back(0)
        





        



        