class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures) 

        for i in range(len(temperatures)):
            while st and st[-1][0] < temperatures[i]:
                x,y = st.pop()
                res[y] = i - y 

            st.append((temperatures[i], i))


        return res
        