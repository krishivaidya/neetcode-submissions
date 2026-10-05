class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def isp(string):
            l = 0
            r = len(string) - 1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(index):
            if index >= len(s):
                res.append(subset.copy())
                return 

            for i in range(index, len(s)):
                if isp(s[index:i + 1]):
                    subset.append(s[index:i + 1])
                    backtrack(i + 1)
                    subset.pop()

        backtrack(0)
        return res

                    


            

        