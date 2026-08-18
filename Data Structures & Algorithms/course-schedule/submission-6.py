class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses 
        adj = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            adj[i[0]].append(i[1])
            indegree[i[1]] += 1

        process = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
               
        

        while q:
            cur = q.popleft()
            process += 1 

            for i in adj[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        return process == numCourses
