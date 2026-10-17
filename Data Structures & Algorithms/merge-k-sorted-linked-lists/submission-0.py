# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:  
    def merge(self, l1, l2):
        p1, p2 = l1, l2
        res = ListNode(-1)
        res_head = res
        while p1 and p2:
            if p1.val < p2.val:
                res.next = ListNode(p1.val)
                res = res.next
                p1 = p1.next
            else:
                res.next = ListNode(p2.val)
                res = res.next
                p2 = p2.next

        while p1:
            res.next = ListNode(p1.val)
            p1 = p1.next
            res = res.next
        while p2:
            res.next = ListNode(p2.val)
            p2 = p2.next
            res = res.next
        return res_head.next
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = deque(lists)

        while queue:
            if len(queue) >= 2:
                l1, l2 = queue.popleft(), queue.popleft()
                queue.append(self.merge(l1,l2))

            else:
                return queue.popleft()

        return None





        