class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) -1]

    def getMin(self) -> int:
        mVal = 2**31 - 1
        for num in self.stack:
            if num < mVal:
                mVal = num

        return mVal
        
