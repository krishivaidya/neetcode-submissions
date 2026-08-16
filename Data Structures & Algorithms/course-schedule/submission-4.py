class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        
        indegree = [0] * numCourses
        adj =[[] for _ in range(numCourses)]
        for i in prerequisites:
            cur = i[0]
            indegree[cur] += 1
            adj[i[1]].append(i[0])

        processed = 0
        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
                processed += 1

        while q:
            
            cur = q.popleft()

            for i in adj[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
                    processed += 1

        if processed == numCourses:
            return True

        return False
            

        