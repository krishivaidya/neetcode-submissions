class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # find the freq of each task and make it a max heap
        freq = {}
        heap = []
        order = []

        for i in tasks:
            freq[i] = freq.get(i, 0) + 1
        
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        q = deque()

        while q or heap:
            # check if a task has finished cooling down
            if q:
                if len(order) + 1 == q[0][1]:
                    whatever = q.popleft()
                    heapq.heappush(heap, whatever[0])

            if heap:
                count, cur_let = heapq.heappop(heap)
                count = -count

                order.append(cur_let)
                count -= 1

                if count > 0:
                    q.append(((-count, cur_let), len(order) + n + 1))

            else:
                order.append(" ")

        return len(order)