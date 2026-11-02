# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        def reorder(front, back):
            if back is None:
                return front

            front = reorder(front, back.next)

            if front is None:  # Already reached the middle
                return None

            if front is back or front.next is back:
                back.next = None
                return None

            next_front = front.next
            front.next = back
            back.next = next_front

            return next_front  # Move front forward

        reorder(head, head)
        