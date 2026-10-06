class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjl = [[] for i in range(numCourses)]
        for a,b in prerequisites:
            adjl[b].append(a)

        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False

            if node in visited:
                return True 

            visiting.add(node)
            visited.add(node)
            

            for child in adjl[node]:
                if not dfs(child):
                    return False 

            visiting.remove(node)
            

            return True 

        for i in range(numCourses):
            if not dfs(i):
                return False 

        return True

                

        