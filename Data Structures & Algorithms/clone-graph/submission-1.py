"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}
        if not node:
            return None

        clone[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for i in cur.neighbors:
                if i not in clone:
                    clone[i] = Node(i.val)
                    q.append(i)
                clone[cur].neighbors.append(clone[i])

        return clone[node]

                