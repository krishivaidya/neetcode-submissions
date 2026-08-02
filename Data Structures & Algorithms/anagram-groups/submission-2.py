class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalhash = {}
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord("a")] += 1

            if tuple(count) in finalhash:
                finalhash[tuple(count)].append(s)
            else:
                finalhash[tuple(count)] = [s]
        
        return list(finalhash.values())




        