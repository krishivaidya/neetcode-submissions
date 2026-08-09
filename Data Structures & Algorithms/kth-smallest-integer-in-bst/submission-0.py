# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def preorder(root):
            
            if not root:
                return res 
            preorder(root.left)
            res.append(root.val)
            preorder(root.right)
        preorder(root)
        return res[k - 1]
            
        