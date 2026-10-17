# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        carry = 0 
        p1, p2 = l1, l2
        res = ListNode(-1)
        res_head = res
        while p1 and p2:
            d1, d2 = p1.val, p2.val
            s = d1 + d2 + carry
            carry = s // 10 
            value = s % 10
            res.next = ListNode(value)
            p1 = p1.next
            p2 = p2.next
            res = res.next

        while p1:
            d1 = p1.val
            s = d1 + carry
            carry = s // 10 
            value = s % 10
            res.next = ListNode(value)
            p1 = p1.next
            res = res.next


        while p2:
            d2 = p2.val
            s = d2 + carry
            carry = s // 10 
            value = s % 10
            res.next = ListNode(value)
            p2 = p2.next
            res = res.next

        if carry:
            res.next = ListNode(carry)
            res = res.next

        return res_head.next
        




        