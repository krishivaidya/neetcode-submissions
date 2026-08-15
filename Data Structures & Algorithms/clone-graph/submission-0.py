"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        create = {}
        if not node:
            return node
        create[node] = Node(node.val)

        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()
            for i in cur.neighbors:
                if i not in create:
                    create[i] = Node(i.val)
                    q.append(i)
                create[cur].neighbors.append(create[i])

        return create[node]

    
            


            

        