class TreeNode:
    
    def __init__(self, data) -> None:
        self.data = data
        self.left = None;
        self.right = None;
        

class BinarySearchTree:
    def __init__(self):
        self.root = None;
        
    # Insertion of binary tree
    
    def insert(self, data):
         self.root = self.insert_node(self.root, data)
         
    def insert_node(self, root, data):
        
        if root is None:
            return TreeNode(data)
        
        if data < root.data:
            root.left = self.insert_node(root.left, data)
        
        if data > root.data:
            root.right = self.insert_node(root.right, data)
                
        return root  
       
        
    def pre_order(self):
        stack = [];
        currentNode = self.root;
        
        while len(stack) > 0 or (currentNode is not None):
            if currentNode is not None:
                stack.append(currentNode);
                currentNode = currentNode.left;
                
            else:
                currentNode = stack.pop()
                print(f'Data: {currentNode.data}', end=", ")
                currentNode = currentNode.right;
     
    def search_node(self, data):
        return self.search(self.root, data)
     
    def search(self, root, data):
        result = None; 
        if (root is None):
            return result
        
        if root.data == data:
            return root
        
          
        if data < root.data:
            return self.search(root.left, data)
        elif data > root.data:
            return self.search(root.right, data)
                    
        
             
        
        


BTS = BinarySearchTree()
BTS.insert(12)
BTS.insert(4)
BTS.insert(8)
BTS.insert(45)
BTS.insert(86)
BTS.insert(3)
BTS.insert(6)
BTS.insert(96)
BTS.insert(3)

BTS.pre_order()
print("")
print(BTS.search_node(43))
print(BTS.search_node(8))
print(BTS.search_node(6))

