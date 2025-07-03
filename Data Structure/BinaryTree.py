from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def construct(self, arr):
        for value in arr:
            self.insert(value)
    
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
        if self.root is None: 
            return
 
        def inOrderStoreValues():
            values = []
            stack = []
            curr = self.root
            while curr is not None or stack:
                if curr is not None:
                    stack.append(curr)
                    curr = curr.left
                else:
                    curr = stack.pop()
                    values.append(curr.value)
                    curr = curr.right
            return values

        def balanceTree(values, start, end):
            if start > end:
                return
            
            mid = (start + end) // 2
            root = Node(values[mid])

            root.left = balanceTree(values, start, mid-1)
            root.right = balanceTree(values, mid+1, end)

            return root

        storeValues=inOrderStoreValues()
        self.root = balanceTree(storeValues, start=0, end=len(storeValues)-1)


    def preOrderTraversal():
        pass

    def inOrderTraversal():
        pass

    def postOrderTraversal():
        pass

    def height(self):
        '''Get the height/depth of the binary tree'''
        pass

    def __str__(self):
        '''
        Returns a displayable string format for the binary tree.
        Format is in array (sequential) representation where keys are ordered by
        top to bottom, left to right of the tree.
        '''

        if self.root is None: 
            return
        
        output = ""
        queue = deque()
        queue.append(self.root)
        while queue:
            curr = queue.popleft()
            output += str(curr.value) + " "
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
            
        return output
    
    def __len__(self):
        '''Returns the number of nodes in the binary tree'''
        return self.length

if __name__ == "__main__":
    tree = BinaryTree()
    tree.construct([5, 3, 4, 2, 1, 6, 0])
    print(tree)
    tree.balance()
    print(tree)
    # tree.insert(10)
    # tree.insert(9)
    # tree.insert(11)
    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.right.value)

'''
TODO:
Test insert and remove functions
Fix print function to include None keys
'''