# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #step1 is to initialise, and make the right pointer n nodes away from the left one. s2 is to make the right one fo till
        dummy = ListNode(0, head)
        left = dummy 
        right = head
        l = n

        for i in range(n):
            right = right.next
        
        while right:
            right = right.next
            left = left.next 

        left.next = left.next.next 
        return dummy.next



             
        

        