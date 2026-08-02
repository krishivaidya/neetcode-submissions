class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")] += 1
            
            if tuple(count) in res: 
                res[tuple(count)].append(i)
            else:
                res[tuple(count)] = [i]
        
        return list(res.values())

        