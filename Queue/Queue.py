class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def enqueue(self, data):
        newNode = Node(data)
        if(self.size == 0):
            self.front = newNode
            self.rear = self.front
            self.size += 1
            return
        self.rear.next = newNode
        self.rear = self.rear.next
        self.size += 1
        
    def dequeue(self):
        if(self.size == 1):
            data = self.front.data
            self.front = None
            self.rear = None
            self.size -= 1
            return data
        
        data = self.front.data
        nextNode = self.front.next
        self.front = nextNode
        self.size -= 1
        
        
    def to_string(self):
        currNode = self.front
        while currNode is not None:
            print(currNode.data, '-->', end=' ' )
            currNode = currNode.next
            
            

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.size)
queue.dequeue()
queue.dequeue()
queue.to_string()
print(queue.size)
            
        
            
        