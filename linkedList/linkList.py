class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.size += 1
            return None

        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = Node(data, None)
        self.size += 1
        return None

    def get_elements(self):
        currentNode = self.head
        data = []
        if currentNode is None:
            return data

        while currentNode is not None:
            data.append(currentNode.data)
            currentNode = currentNode.next
        return data

    def insertAt(self, index, data):
        try:

            if index > self.size + 1 or index < 1:
                print(index)
                raise IndexError()

            if index == self.size + 1:
                return self.append(data)
            if index == 1:
                return self.prepend(data)

            pointer = index - 1
            currentNode = self.head
            while pointer > 1:
                currentNode = currentNode.next
                pointer -= 1
            newNode = Node(data, currentNode.next)
            currentNode.next = newNode
            self.size += 1
            return None
        except IndexError:
            print(f"IndexError: Index out of range. Insert in range 1 to {
                  self.size + 1}")

    def prepend(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return None

    def getAt(self, index):
        if index > self.size or index < 1:
            return 'undefined'

        if index == 1:
            return self.head.data

        currentNode = self.head
        for i in range(1, index):
            currentNode = currentNode.next

        return (currentNode.data)

    def indexOf(self, data):
        currentNode = self.head
        index = 1
        while currentNode.data != data:
            currentNode = currentNode.next
            index += 1
            if not currentNode:
                return 'undefined'
        return (index)

    def indicesOf(self, data):
        currentNode = self.head
        indices = []
        pointer = 1
        while currentNode is not None:
            if currentNode.data == data:
                indices.append(pointer)
            currentNode = currentNode.next
            pointer += 1
        return indices

    def pop(self):
        currentNode = self.head
        while currentNode.next.next is not None:
            currentNode = currentNode.next
        removedNode = currentNode.next
        currentNode.next = None
        return(removedNode.data)
    
    def unshift(self):
        currentNode = self.head
        self.head = currentNode.next
        return currentNode.data
 
    def removedAt(self, *index):
        print(index)

linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)

linkedList.append(4)
linkedList.append(5)
linkedList.append(6)
linkedList.append(7)
linkedList.append(8)
linkedList.prepend(0)
linkedList.insertAt(4, 3)
linkedList.insertAt(10, 9)
linkedList.append(7)


print(linkedList.get_elements())
print(linkedList.removedAt(1,3,5,6,7,8,8))

