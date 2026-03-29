class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        #create dummy node
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        #if head & tail are pointing to the same node that means that there is no real node in b/w
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        #we will keep the dummy nodes, so will insert before the tail node
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node #like this we entered the node b/w head & tail
        first_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        target_node = self.tail.prev
        value = target_node.value

        #previous pointer of the node popped
        prev_node = target_node.prev
        #now we remove the node
        # we can do this by shifting pointers
        prev_node.next = self.tail
        self.tail.prev = prev_node

        #we return the node that is popped
        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        target_node = self.head.next
        value = target_node.value
        next_node = target_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value
