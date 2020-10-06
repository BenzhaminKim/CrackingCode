class Stack():
    def __init__(self):
        self.stack = []
        self.min = float('inf')
        
    def push(self,val):
        if val < self.min:
            self.min = val
        self.stack.append(val)
        print(f"Stack is {self.stack}, min is {self.min}")
        return self.stack

    def pop(self):
        popedNum = self.stack.pop()
        self.min = float('inf')
        for val in self.stack:
            if val < self.min:
                self.min = val
        print(f"Stack is {self.stack}, min is {self.min}")
        return popedNum
    

if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(3)
    stack1.push(2)
    stack1.push(1)
    stack1.pop()