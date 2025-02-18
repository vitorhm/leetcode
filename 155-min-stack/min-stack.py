class MinStack:

    def __init__(self):
        self.arr = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        
        if not self.minimums:
            self.minimums.append(val)
        else:
            if val <= self.minimums[-1]:
                self.minimums.append(val)

    def pop(self) -> None:
        if self.arr[-1] == self.minimums[-1]:
            self.minimums.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()