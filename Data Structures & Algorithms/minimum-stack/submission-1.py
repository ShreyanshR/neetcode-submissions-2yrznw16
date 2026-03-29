class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        le = len(self.stack)
        return self.stack[le-1]

    def getMin(self) -> int:
        m = 2147483647
        for x in self.stack:
            if x < m:
                m = x

        return m
        
