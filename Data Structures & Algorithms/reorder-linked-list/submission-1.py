# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            prev = None
            nex = None 
            curr = head

            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex


            return prev

        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tmp = slow.next
        slow.next = None
        second_start = reverse(tmp)
        curr = head 

        while second_start:
            tmp1, tmp2 = curr.next, second_start.next
            curr.next = second_start
            second_start.next = tmp1
            curr, second_start = tmp1, tmp2

        

        
