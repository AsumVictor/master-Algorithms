from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order(self):
        if self.data is None:
            return

        if self.left is not None:
            self.left.in_order()
        print(self.data)
        if self.right is not None:
            self.right.in_order()

    def in_order_stack(self):

        stack = []
        temp = self

        while len(stack) >= 1 or (temp is not None):
            if temp is not None:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(f"Data: {temp.data}")
                temp = temp.right

    def post_order(self):

        if self.left is not None:
            self.left.post_order()

        if self.right is not None:
            self.right.post_order()

        print(f'Data: {self.data}')

        return

    def post_order_stack(self):

        current = self
        stack = []

        while (current is not None) or (len(stack) >= 1):

            if current is not None:
                stack.append(current)
                current = current.left
            else:
                temp = stack[-1].right

                if temp is None:
                    temp = stack.pop()
                    print(f'Data: {temp.data}')

                    while (len(stack) >= 1) and temp == stack[-1].right:
                        temp = stack.pop()
                        print(f'Data: {temp.data}')

                else:
                    current = temp

    def level_order(self):

        queue = []
        queue.append(self)

        while len(queue) > 0:
            temp = queue.pop(0)
            print(f"Data: {temp.data}")

            if temp.left is not None:
                queue.append(temp.left)

            if temp.right is not None:
                queue.append(temp.right)
    
    def find_max(self):
        
        result = self.data;
        
        left = None;
        if self.left is not None:
            left = self.left.find_max()
        else:
            left = float("-inf")
            
        right = None;
        if self.right is not None:
            right = self.right.find_max()
        else:
            right = float("-inf")
            
        if left > result:
            result = left
            
        if right > result:
            result = right
            
        return result
            
        
        



root = TreeNode(1)
L1 = TreeNode(2)
R1 = TreeNode(3)
LL1 = TreeNode(4)
LR1 = TreeNode(15)
RL1 = TreeNode(6)
RLL1 = TreeNode(7)

root.left = L1
root.right = R1
L1.left = LL1
L1.right = LR1

R1.left = RL1
RL1.left = RLL1

# root.in_order()
# print("-----------------------")
# root.in_order_stack()
# print("-----------------------")
# root.level_order()
print(root.find_max())
