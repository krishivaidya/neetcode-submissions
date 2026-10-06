class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjl = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for a,b in prerequisites:
            adjl[b].append(a)
            indegree[a] += 1
            

        q = deque()
        count = 0

        for ind in range(len(indegree)):
            if indegree[ind] == 0:
                q.append(ind)

        while q:
            cur = q.popleft()
            count += 1

            for child in adjl[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)

        return count == numCourses



        

       