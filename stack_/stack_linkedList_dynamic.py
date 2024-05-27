class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:

    def __init__(self):
        self.stack = LinkedList()
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        if self.stack.head is None:
            self.stack.head = newNode
            self.size += 1
            return None

        currNode = self.stack.head

        while currNode.next is not None:
            currNode = currNode.next

        currNode.next = newNode
        self.size += 1

        return None

    def show(self):
        currNode = self.stack.head
        stack = []
        while currNode is not None:
            stack.append(currNode.data)
            currNode = currNode.next

        return stack

    def top(self):
        currNode = self.stack.head
        while currNode.next is not None:
            currNode = currNode.next

        return currNode.data

    def pop(self):
        print(self.size)
        if self.isEmpty():
            raise Exception('Stack is empty')

        if self.size == 1:
            data = self.stack.head
            self.stack.head = None
            self.size = 0

            return data

        currNode = self.stack.head
        while currNode.next.next is not None:
            currNode = currNode.next

        data = currNode.next.data
        currNode.next = None
        self.size -= 1
        return data

    def isEmpty(self):
        return self.size == 0

    def length(self):
        return (self.size)


stack = Stack()
stack.push('<<Empty>>')
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(12)
stack.push(10)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
