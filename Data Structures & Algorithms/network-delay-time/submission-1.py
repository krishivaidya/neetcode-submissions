class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+ 1)}
        for u,v,w in times:
            adj[u].append((w,v))


        heap = [(0,k)]
        visit = set()
        dist = {}

        while heap:
            wt, t = heapq.heappop(heap)
            if t in visit:
                continue

            visit.add(t)
            dist[t] = wt
            for adjw,adjn in adj[t]:
                new_dist = adjw + wt
                if adjn not in visit and new_dist < dist.get(adjn,float("inf")):
                    heapq.heappush(heap,(new_dist, adjn))

        return max(dist.values()) if len(visit) == n else -1





        