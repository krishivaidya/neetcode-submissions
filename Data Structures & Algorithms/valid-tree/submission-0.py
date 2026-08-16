class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visit = set()

        #create adjacency list
        map = {i:[] for i in range(n)}
        for n1,n2 in edges:
            map[n1].append(n2)
            map[n2].append(n1)

      

        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i) 

            for j in map[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False 

            return True

        if dfs(0,-1) and len(visit) == n:
            return True

        return False

        


        

        



        