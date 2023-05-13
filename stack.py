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

# Question: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def isValid(s):
    #we would need to use a stack to check if an open parantheses is
    #followed by a close one or not, finally on checking all characters
    #if the stack is empty it is valid
    #we would also use a dict to map closing to opening parantheses
    stack=[]
    closeToOpenMap = {')':'(',']':'[','}':'{'}
    #loop through the characters
    for character in s:
        #check if it is an open parantheses
        if character not in closeToOpenMap:
            stack.append(character)
        else:
            #check if the stack is not empty
            #and check if the char put on top of stack is open parantheses
            if stack and stack[-1]==closeToOpenMap[character]:
                #if so remove the char from the top of stack
                stack.pop()
            #else means the no matching parantheses found
            else:
                return False
    return True if not stack else False
