# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        
        while q:
            level = []
            q_len = len(q)
            for _ in range(q_len):
                cur = q.popleft()
                level.append(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            lev_length = len(level)
            node_to_add = level[lev_length - 1]
            res.append(node_to_add.val)
        
        return res
            
        