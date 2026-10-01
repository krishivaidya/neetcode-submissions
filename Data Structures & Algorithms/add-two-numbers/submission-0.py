# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry == 1:
            if l1 and l2:
                add = l1.val + l2.val + carry 
            elif l1:
                add = l1.val + carry 

            elif l2:
                add = l2.val + carry 
            else:
                add = carry 

            if add > 9:
                digit = add % 10
                carry = 1
            else:
                digit = add
                carry = 0


            cur.next = ListNode(digit)
            cur = cur.next
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next

        return dummy.next

    


        