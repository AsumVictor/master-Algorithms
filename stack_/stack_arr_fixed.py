# Dynamic size
class Stack:
    def __init__(self, size):
        self.data = []
        self.max_size = size
        self.size = 0

    def push(self, n):
        if self.isFull():
            raise Exception('Stack is full')
        self.data.append(n)
        self.size += 1
        return None

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')

        self.data.pop()
        self.size -= 1
        return None

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def top(self):
        return self.data[self.size - 1]

    def show(self):
        return self.data

    def length(self):
        return (self.size)


stack = Stack(4)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(14)
stack.pop()
stack.push(14)
print(stack.isFull())
stack.push(14)