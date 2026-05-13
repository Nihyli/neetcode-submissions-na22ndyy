class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head)
        self.head = node
        

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        
        i = 0
        curr = self.head
        while curr and curr.next:
            if i + 1 == index:
                curr.next = curr.next.next
                return True
            curr = curr.next
            i += 1
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
