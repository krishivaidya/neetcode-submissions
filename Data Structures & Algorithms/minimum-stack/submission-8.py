class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack= []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        newmin = 0
        if self.minstack and val > self.minstack[-1]:
            new_min = self.minstack[-1]
        else:
            new_min = val
        self.minstack.append(new_min)
        

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

        
