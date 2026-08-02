# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        check = set()
        while cur:
            if cur in check:
                return True
            else:
                check.add(cur)
                cur = cur.next
        return False
        