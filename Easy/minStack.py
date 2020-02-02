class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or self.minstack[-1] >= x:
            self.minstack.append(x)

    def pop(self) -> None:
        top = self.top()
        del self.stack[-1]

        if top == self.minstack[-1]:
            del self.minstack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()