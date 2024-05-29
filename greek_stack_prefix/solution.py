# Stack
class StackNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Stack:
      def __init__(self):
           self.root = None
           self.size = 0
           
      def push(self, data):
          stackNode = StackNode(data)
          if self.root == None:
            self.root = stackNode
            return None
        
          stackNode.next = self.root
          self.root = stackNode
          self.size += 1
          return None
          
      def pop(self):
          if self.isEmpty():
              return None
          
          topNode = self.root.data
          self.root = self.root.next
          print(self.root.data)
          self.size -= 1
          return topNode
      
    
      def isEmpty(self):
         return self.size == 0
          
def addOperand(oprnd):
    if oprnd is None:
        return ''
    
    return oprnd

def solution(exp):
    res = ''
    operations = {'+','/','-','*'}
    stack = Stack()
    for char in exp:
        if char not in operations:
            stack.push(char)
        else:
            res += char
            stack.pop()
            stack.pop()
            # op2 = stack.pop()
            # res += addOperand(stack.pop())
            # res += addOperand(stack.pop())
            
    # print(res)
            
    
        

solution('AB+CD-*')
# *+AB-CD
