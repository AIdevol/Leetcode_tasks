class MinStack:
    def __init__(self):
        self.stack = []  # initialize main stack
        self.min_stack = []  # initialize minimum value stack

    def push(self, val: int) -> None:
        self.stack.append(val)  # push value onto main stack
        if not self.min_stack or val <= self.min_stack[-1]:  # if minimum stack is empty or the value is smaller or equal to current minimum
            self.min_stack.append(val)  # push value onto minimum stack

    def pop(self) -> None:
        if self.stack:  # check if main stack is not empty
            if self.stack[-1] == self.min_stack[-1]:  # if the element to pop is the current minimum
                self.min_stack.pop()  # pop from minimum stack
            self.stack.pop()  # always pop from main stack

    def top(self) -> int:
        if self.stack:  # check if main stack is not empty
            return self.stack[-1]  # return the top element

    def getMin(self) -> int:
        if self.min_stack:  # check if minimum stack is not empty
            return self.min_stack[-1]  # return the current minimum value
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()