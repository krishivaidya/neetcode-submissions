class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')

        # dist[v] = cheapest price found so far to reach airport v
        dist = [INF] * n
        dist[src] = 0                      # you start at src for free

        # K stops = K+1 flights = K+1 rounds
        for _ in range(k + 1):
            prev = dist[:]                 # snapshot: freeze last round's prices

            for u, v, w in flights:        # flight u -> v costs w
                if prev[u] != INF and prev[u] + w < dist[v]:
                    dist[v] = prev[u] + w  # cheaper way to reach v with one more flight

        return dist[dst] if dist[dst] != INF else -1

            

        






        