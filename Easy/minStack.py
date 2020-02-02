class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minE = float("inf")
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minE = min(x, self.minE)

    def pop(self) -> None:
        top = self.top()
        del self.stack[-1]

        if len(self.stack):
            self.minE = min(self.stack)
        else:
            self.minE = float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minE

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()