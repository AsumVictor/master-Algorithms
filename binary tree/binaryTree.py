class Tree:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        
    def insertNode(self, data):
          if self.data is None:
              self.data = data
              return None
          
          newNode = Tree()
          newNode.insertNode(data)

          if data <= self.data:
              
              if self.left is None:
                  self.left = newNode
              else:
                  self.left.insertNode(data)
                  
          else:
              if self.right is None:
                  self.right = newNode
              else:
                  self.right.insertNode(data)
      
    def getNodes(self):
        data = {}  
        
        if self.data is None:
            return None 
        
        data['root'] = self.data
        if self.left is None:
            data['left'] = None
        else:
            data['left'] = self.left.getNodes()
        
        if self.right is None:
            data['right'] = None
        else:
            data['right'] = self.right.getNodes()
            
        return data
    
    
    
    

root = Tree()
root.insertNode(20)
root.insertNode(12)
root.insertNode(33)
root.insertNode(44)
root.insertNode(6)

root.insertNode(6)
root.insertNode(17)
root.insertNode(22)


nodes = root.getNodes()
print(nodes)

