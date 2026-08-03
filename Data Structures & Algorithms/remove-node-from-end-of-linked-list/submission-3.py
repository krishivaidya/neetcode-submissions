# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        noofnodes = 1
        while right and right.next:
            noofnodes += 1
            right = right.next
        
        if noofnodes == 1 and n == 1:
            del right 
            return None

        prev = ListNode()
        posofleft = 0

        while noofnodes - posofleft != n and left and left.next:
            prev = left
            left = left.next 
            posofleft += 1
        
        prev.next = left.next
        if left == head:
            del left
            return prev.next
        else:
            return head
            
             
        

        