# Implementation of queue using python list without fixed capacity

# class Queue:
#     def __init__(self):
#         self.items = []

#     def __str__(self):
#         values = [str(x) for x in self.items]
#         return ' '.join(values)

#     def isEmpty(self):
#         if len(self.items) == 0:
#             return True
#         else:
#             return False

#     def enqueue(self, val):
#         self.items.append(val)
#         return 'The element is inserted at the end of the queue'

#     def dequeue(self):
#         if self.isEmpty():
#             return False
#         else:
#             self.items.pop(0)
#             return 'The element is removed from the front of the queue'

#     def delete(self):
#         self.items = None


# customQueue = Queue()
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# customQueue.enqueue(4)
# customQueue.enqueue(5)
# customQueue.dequeue()
# print(customQueue)


# Implementation of queue using python list with fixed capacity (circular queue)

# class Queue:
#     def __init__(self, maxSize):
#         self.items = maxSize * [None]
#         self.maxSize = maxSize
#         self.start = -1
#         self.top = -1

#     def __str__(self):
#         values = [str(x) for x in self.items]
#         return ' '.join(values)

#     def isFull(self):
#         # condition1: if top of list is behind start of list and no gap between
#         if self.top + 1 == self.start:
#             return True
#         # condition2: if start at 0th index and top at last index
#         elif self.start == 0 and self.top + 1 == self.maxSize:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if self.top == -1:
#             return True
#         else:
#             return False

#     def enqueue(self, val):
#         if self.isFull():
#             return 'The queue is full'
#         else:
#             if self.top + 1 == self.maxSize:
#                 self.top = 0
#             else:
#                 self.top += 1
#                 if self.start == -1:
#                     self.start = 0
#             self.items[self.top] = val
#             return 'the value has been enqueued at the end of the queue'

#     def dequeue(self):
#         if self.isEmpty():
#             return 'The queue is empty'
#         else:
#             firstElement = self.items[self.start]
#             start = self.start
#             if self.start != self.top:
#                 self.start += 1
#             elif self.start == self.top:
#                 self.start = -1
#                 self.top = -1
#             elif self.start + 1 == self.maxSize:
#                 self.start = 0
#             self.items[start] = None
#             return firstElement

#     def delete(self):
#         self.items = self.maxSize * [None]
#         self.top = -1
#         self.start = -1


# customQueue = Queue(5)
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# customQueue.enqueue(4)
# customQueue.enqueue(5)
# print(customQueue)

# print(customQueue.dequeue())
# print(customQueue)


# Implementation of queue using linked list

# create a node class
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.value)


# create a linkedlist class
class LinkedList:
    # fn to initialize head and tail
    def __init__(self):
        self.head = None
        self.tail = None

    # To make the linkedlist we create printable
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


# create a queue using linkedlist
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
