class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        store = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while store and temperatures[i] > store[-1][0]:
                stackT, stackInd = store.pop()
                result[stackInd] = i - stackInd
            
            store.append((temperatures[i], i))
        return result



        