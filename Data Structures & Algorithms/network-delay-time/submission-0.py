class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build the adjacency list 
        adj = {i: [] for i in range(1,n + 1)}
        for u,v,w in times:
            adj[u].append((w,v))


        heap = [(0,k)]
        dist = {}

        while heap:
            w,u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = w
            for t,v in adj.get(u,[]):
                if v not in dist:
                    heapq.heappush(heap,(t + dist[u], v))

        return max(dist.values()) if len(dist) == n else -1


        