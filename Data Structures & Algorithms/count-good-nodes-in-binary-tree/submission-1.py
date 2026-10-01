# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = []
        stack.append((root,float("-inf")))
        count = 0

        while stack:
            cur, curmax = stack.pop()
            if cur.val >= curmax:
                count += 1
                curmax = cur.val

            if cur.left:
                stack.append((cur.left,curmax))

            if cur.right:
                stack.append((cur.right,curmax))


        return count

            


            
            
                

            

        