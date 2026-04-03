# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        extraNode = ListNode(0, head)
        ptr1 = tail = extraNode

        for i in range (n+1):
            tail = tail.next
        
        while tail:
            tail = tail.next
            ptr1 = ptr1.next
            
        ptr1.next = ptr1.next.next
        

        return extraNode.next
        