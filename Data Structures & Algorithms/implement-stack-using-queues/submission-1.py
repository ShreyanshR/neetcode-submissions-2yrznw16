class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyStack:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next= self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:
        new_node = Node(x)

        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node

        new_node.next = self.tail
        self.tail.prev = new_node
        

    def pop(self) -> int:
        if self.empty():
            return -1

        last_node = self.tail.prev
        value = last_node.val

        prev_node = last_node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value
        

    def top(self) -> int:
        last_node = self.tail.prev

        value = last_node.val

        return value

    def empty(self) -> bool:
        return self.head.next == self.tail
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()