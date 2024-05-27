# Dynamic size
class Stack:
    def __init__(self):
        self.data = []
        self.size = 0
        
    def push(self, n):
        self.data.append(n)
        self.size += 1
        return None
    
    def pop(self):
        if not self.isEmpty():
            self.data.pop()
            self.size -= 1

        return None
    
    def isEmpty(self):
        return self.size == 0
    
    def top(self):
        return self.data[self.size - 1]
    
    def show(self):
        return self.data
    
    def length(self):
        return (self.size)
        
        
        
        
stack = Stack()
stack.push('Victor')
stack.push(4)
stack.push(0)
stack.push('Jescaprd')
stack.push(90)
stack.push(190)
stack.push('Showing now')
stack.push(77)
stack.push(77)
stack.pop()
stack.pop()
stack.pop()
print(stack.top())
