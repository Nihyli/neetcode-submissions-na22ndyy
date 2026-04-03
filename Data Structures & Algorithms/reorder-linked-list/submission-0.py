# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        traverse = head
        hold = []
        while traverse:
            hold.append(traverse)
            traverse = traverse.next
        
        i,j = 0, len(hold)-1
        while i < j:
            hold[i].next = hold[j]
            i += 1
            if i >= j :
                break
            hold[j].next = hold[i]
            j -= 1
        
        hold[i].next = None

