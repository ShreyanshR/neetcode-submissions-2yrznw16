class ListNode:
    def __init__(self, val, next_node=None):
        self.next = next_node
        self.value = val

class LinkedList:
    def __init__(self):
        # A dummy node is created to remove from the beginning of Linked List
        self.head = ListNode(-1)
        #in the beginning head = tail
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i=0
        while curr:
            if i == index:
                return curr.value
            i+=1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if not new_node.next:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while i < index and curr:
            #this loop will run until index is = i
            #this will only exit when we found which element to remove
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                #if there are only two elements or one
                #tail will become the current
                self.tail = curr

            curr.next = curr.next.next
            return True

        return False

        

    def getValues(self) -> List[int]:
        curr = self.head.next
        ele = []
        while curr:
            ele.append(curr.value)
            curr = curr.next

        return ele
