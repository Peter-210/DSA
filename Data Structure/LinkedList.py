class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def construct(self, arr):
        for i in range(len(arr)-1, -1, -1):
            self.appendleft(arr[i])

    def appendleft(self, value):
        '''Adds an element to the start of a linked list'''

        newNode = Node(value)
        self.length += 1
        if self.head is None:
            self.head = newNode
        else:
            tempNode = self.head
            self.head = newNode
            newNode.next = tempNode
    
    def append(self, value):
        '''Adds an element to the end of a linked list'''

        self.length += 1
        if self.head is None:
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value)

    def insert(self, pos, value):
        '''Adds an element to the linked list based on the specified index'''
        if pos > self.length:
            raise Exception("Index of out bounds")
        
        if pos == 0:
            self.appendleft(value)
        elif pos == self.length:
            self.append(value)
        else:
            curr = self.head
            for _ in range(pos-1):
                curr = curr.next
            
            tempNode = curr.next
            curr.next = Node(value)
            curr.next.next = tempNode

    def remove(self):
        '''Removes the first element of the linked list'''

        if self.length == 0:
            raise Exception("Linked list has no element to remove")
        
        self.length -= 1
        node = self.head
        self.head = node.next
        return node.value

    def pop(self):
        '''Removes the last element of the linked list'''

        if self.length == 0:
            raise Exception("Linked list has no element to remove")
        
        self.length -= 1

        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        
        else:
            prev = self.head
            curr = prev.next
            
            while curr.next is not None:
                prev = curr
                curr = curr.next
            
            prev.next = None
            return curr.value

    def popAtIndex(self, pos):
        '''Removes an element from the linked list based on the specified index'''
        if pos > self.length - 1:
            raise Exception("Index of out bounds")
        
        if pos == 0:
            return self.remove()
        elif pos == self.length - 1:
            return self.pop()
        else:
            self.length -= 1
            curr = self.head
            for _ in range(pos-1):
                curr = curr.next
            
            value = curr.next.value
            curr.next = curr.next.next
            return value

    def update(self, pos, value):
        '''Update an element in the linked list based on the specified index'''
        if pos > self.length - 1:
            raise Exception("Index of out bounds")
        
        if pos == 0:
            self.head.value = value
        else:
            curr = self.head
            for _ in range(pos):
                curr = curr.next
            curr.value = value

    def peek(self):
        '''Look at the first element in the linked list'''
        return self.head.value
    
    def index(self, pos):
        '''Look at an element in the linked list based on the specified index'''
        if pos > self.length - 1:
            raise Exception("Index of out bounds")
        
        if pos == 0:
            return self.head.value
        else:
            curr = self.head
            for _ in range(pos):
                curr = curr.next
            return curr.value

    def reverse(self):
        '''Reverses the order of the linked list'''
        if self.length <= 1: return

        curr = self.head
        prev = None
        while curr is not None:
            nextNode = curr.next
            curr.next = prev

            prev = curr
            curr = nextNode

        self.head = prev
            
    def __str__(self):
        '''Returns a displayable string format for the linked list'''

        output = ""
        curr = self.head

        while curr is not None:
            output += str(curr.value) + " "
            curr = curr.next

        return output
    
    def __len__(self):
        '''Returns the length of a linked list'''
        return self.length


if __name__=="__main__":
    linkedList = LinkedList()
    linkedList.construct([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(linkedList)
    