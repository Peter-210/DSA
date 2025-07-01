# https://www.geeksforgeeks.org/python/python-linked-list/

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

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

    def pop(self, pos):
        '''Removes an element from the linked list based on the specified index'''
        pass
        # if pos > self.length - 1:
        #     raise Exception("Index of out bounds")
        
        # if pos == 0:
        #     return self.remove()
        # elif pos == self.length - 1:
        #     return self.pop()
        # else:
        #     curr = self.head
        #     for _ in range(pos-1):
        #         curr = curr.next
            
        #     tempNode = curr.next
        #     curr.next = Node(value)
        #     curr.next.next = tempNode

    def reverse(self):
        '''Reverses the order of the linked list'''
        pass

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
    linkedList.appendleft(8)
    linkedList.appendleft(7)
    linkedList.appendleft(6)
    linkedList.appendleft(5)
    linkedList.appendleft(4)
    linkedList.appendleft(3)
    linkedList.appendleft(2)
    linkedList.appendleft(1)
    linkedList.appendleft(0)
    linkedList.insert(11, 1020)
    print(linkedList)