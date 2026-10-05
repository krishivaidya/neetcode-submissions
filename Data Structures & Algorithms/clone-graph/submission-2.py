"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        store = {}
        if not node:
            return None

        q = deque([node])

        while q:
            cur = q.pop()
            store[cur] = Node(cur.val)

            for i in cur.neighbors:
                if i not in store:
                    q.append(i)

        for key in store.keys():
            for i in key.neighbors:
                store[key].neighbors.append(store[i])

        return store[node]

        

                    
        