class Stack:
    def __init__(self, data=None):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack)>0:
            data = self.stack[-1]
            del self.stack[-1]
            return data
        else:
            return ('Stack is empty!')

    def peek(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return ('Stack is empty!')

s1 = Stack()
s1.push(10)
s1.push(11)
print(s1.peek())
print(s1.pop())
print(s1.peek())
