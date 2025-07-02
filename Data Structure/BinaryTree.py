class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        '''Add the specified element to the binary tree'''
        if self.root is None:
            self.root = Node(value)
            return
        
        stack = [self.root]
        while stack:
            curr = stack.pop()
            if curr.value < value:
                if curr.right is None:
                    curr.right = Node(value)
                else:
                    stack.append(curr.right)
            else:
                if curr.left is None:
                    curr.left = Node(value)
                else:
                    stack.append(curr.left)

    def remove(self, value):
        '''Remove the specified element from the binary tree'''
        if self.root is None: 
            return
        
        stack = [self.root]
        while stack:
            curr = stack.pop()
            if curr.value == value:
                if curr.left == None and curr.right == None:
                    del curr
                    return
                
                if curr.left == None:
                    curr = curr.right
                    return
                
                if curr.right == None:
                    curr = curr.left
                    return
                
            if curr.value < value and curr.right is not None:
                stack.append(curr.right)
                continue

            if curr.value > value and curr.left is not None:
                stack.append(curr.left)
                continue
            

    def balance(self):
        '''Balance the tree as a complete binary tree'''
        pass

    def height(self):
        '''Get the height/depth of the binary tree'''
        pass

    def __str__(self):
        '''Returns a displayable string format for the binary tree'''

        pass

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(9)
    tree.insert(11)
    print(tree.root.value)
    print(tree.root.left.value)
    print(tree.root.right.value)

'''
TODO:
Test insert and remove functions
'''