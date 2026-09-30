class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        minval = val
        if self.minstack:
            minval = min(self.minstack[-1], val)
        self.minstack.append(minval)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minstack:
            self.minstack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        
