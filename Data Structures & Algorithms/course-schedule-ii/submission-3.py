class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        res = []
        indegree = [0] * numCourses

        for i in prerequisites:
            adj[i[1]].append(i[0])
            indegree[i[0]] += 1

        q = deque()
        for a,i in enumerate(indegree):
            if i == 0:
                q.append(a)

        while q:
            cur = q.popleft()
            res.append(cur)

            for i in adj[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        if len(res) == numCourses:
            return res

        else:
            return []



        

        
        
        