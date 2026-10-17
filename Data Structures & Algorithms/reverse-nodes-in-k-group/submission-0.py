class Solution:
    def reverse(self, head, end_node):
        prev = end_node
        curr = head
        while curr != end_node:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_tail = dummy
        window_head = head
        curr = head
        n = 0

        while curr:
            n += 1
            if n % k == 0:
                next_start = curr.next
                group_head = self.reverse(window_head, next_start)

                prev_tail.next = group_head   # link previous group to this one
                prev_tail = window_head       # old start is now this group's tail
                window_head = next_start      # next window begins here
                curr = next_start             # jump forward, don't step backward
            else:
                curr = curr.next

        return dummy.next