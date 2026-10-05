class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def check(start, end):
            checks = s[start:end]
            for word in wordDict:
                if word == checks:
                    return True
            return False

        split = [False] * (len(s) + 1)
        split[len(s)] = True
        for index in range(len(s) - 1, -1, -1):
            for end in range(index + 1, len(s) + 1):
                if check(index, end) and split[end]:
                    split[index] = True
                    break

        return split[0]

    



        