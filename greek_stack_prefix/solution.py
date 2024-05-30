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
            self.size += 1
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
          self.size -= 1
          return topNode
      
    
      def isEmpty(self):
         return self.size == 0
     
      def show(self):
          node = self.root
          res = []
          while node is not None:
              res.append(node.data)
              node = node.next
              
          return res
          
       
def solution(exp):
    operations = {'+','/','-','*'}
    stack = Stack()
    for char in exp:
        if char in operations:
            operand2 = (stack.pop())
            operand1 = (stack.pop())
            res = ''
            res += char
            res += operand1
            res += operand2
            stack.push(res)
        else:
         stack.push(char)
          
    return (stack.pop())
            
    
        

# solution('AB+CD-*')
# # *+AB-CD

# solution('ABC/-AK/L-*')
# # *-A/BC-/AKL
