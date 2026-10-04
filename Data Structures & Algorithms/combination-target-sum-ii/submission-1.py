class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def back(index, target):
            if target == 0:
                res.append(subset.copy()) 
                return 

            if index >= len(candidates) or target < 0:
                return 

            subset.append(candidates[index])
            back(index + 1, target - candidates[index])
            subset.pop()
            
            index = index + 1 
            while index < len(candidates) and  candidates[index] == candidates[index - 1]:
                index += 1
            back(index, target)

        
        back (0,target)
        return res


        