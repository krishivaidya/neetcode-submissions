class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        store = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        i = 0
        self.s = ""
        if len(digits) == 0:
            return []
        def back(i):
            if len(digits) == len(self.s):
                self.res.append(self.s)
                return 

            values = store[(digits[i])]
            length = len(values)
            for ind in range(length):
                self.s += values[ind] 
                back(i + 1)
                self.s = self.s[:-1]
            
        back(0)
        return self.res

        