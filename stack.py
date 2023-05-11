#implementation of stack using list 
customStack = []
customStack.append(1)
customStack.append(2)
customStack.append(3)
customStack.append(4)
print(customStack)
customStack.pop()


customStack.pop() if len(customStack)  else print("empty")
print(customStack)
print(type(customStack))

#implementation of stack using dequeu
from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)


#create stack using list w/o size limit
#performance leaks as the size of the list grows
class stack:
    def __init__(self):
        self.list = []
    

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    #isEmpty method
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    #push
    def add(self,element):
        self.list.append(element)
        return "The element has been successfully added"
stackNew = stack()
print(stackNew.isEmpty())
stackNew.add(100)
stackNew.add(200)
stackNew.add(300)
print(stackNew)


#create stack using python list with size limit
class stackLimit:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    #is empty method same

    #isFull method
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False

     #push
    def add(self,element):
        if self.isFull():
            return "Stack is Full"
        self.list.append(element)
        return "The element has been successfully added"

customStack = stackLimit(5)
customStack.add(4)
customStack.add(4)
customStack.add(4)
customStack.add(4)
customStack.add(4)
customStack.add(4)
customStack.add(4)
print(customStack)  


#create stack using linkedlist
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node = node.next
class StackLinkedList:
    #creates stack using linkedList
    def __init__(self):
        self.SLL = SLL()
    
    def isEmpty(self):
        if self.SLL.head == None:
            return True
        return False
    def __str__(self):
        
        values = [str(x.value) for x in self.SLL]
        return '\n'.join(values)
    
    def add(self,value):
        newNode = Node(value)
        newNode.next = self.SLL.head
        self.SLL.head = newNode

    def pop(self):
        if self.isEmpty():
            return "list empty"
        else:
            nodeValue = self.SLL.head.value
            self.SLL.head = self.SLL.head.next
            return nodeValue
    def peek(self):
        if self.isEmpty():
            return "list empty"
        else:
            nodeValue = self.SLL.head.value
            
            return nodeValue
    def delete(self):
        self.SLL.head = None
customStack = StackLinkedList()
print(customStack.isEmpty())
customStack.add(1)
customStack.add(2)
customStack.add(3)
customStack.add(4)
customStack.add(5)
customStack.add(6)
customStack.add(7)
customStack.pop()
print(customStack.peek())
print(customStack)  
# customStack.delete()
# print(customStack)
print(type(customStack))