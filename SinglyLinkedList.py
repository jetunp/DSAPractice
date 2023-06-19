# # create a node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


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

    # traversing a linkedlist
    def traverse(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.val)
                node = node.next

    def countNodes(self):
        count = 0
        dummy = self.head
        while dummy:
            count += 1
            dummy = dummy.next
        return count

    # inserting a node to linkedlist

    def insertNode(self, val, position):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if position == 0:
                print("position 0")
                new_node.next = self.head
                self.head = new_node
            elif position == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            elif position > self.countNodes():
                raise TypeError(
                    f"cannot add node to a position: {position} greater than length of node: {self.countNodes()}")
            else:
                dummy_node = self.head
                index = 0
                while index < position - 1:
                    dummy_node = dummy_node.next
                    index += 1
                next_node = dummy_node.next
                dummy_node.next = new_node
                new_node.next = next_node
                if dummy_node == self.tail:
                    self.tail = new_node

    # search through the linkedlist for a node
    def searchNode(self, nodeValue):
        if self.head is None:
            print("the list is empty")
        else:
            node = self.head
            while node is not None:
                if node.val == nodeValue:
                    return node.val
                else:
                    node = node.next
            return "node does not exist"

    # delete one node from the linkedlist
    def deleteNode(self, position):
        if self.head is None:
            print("the list does not exist")
        else:
            if position == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif position >= self.countNodes():
                raise TypeError(
                    f"cannot delete node from a position(0-indexed): {position} greater than or equal to length of node: {self.countNodes()}")
            else:
                print("grerjer")
                temp_node = self.head
                index = 0
                while index < position-1:
                    # traversing through list everytime it will take value of the next node on the list
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    # delete the entire linked list

    def deleteList(self):
        self.head = None
        self.tail = None


sll1 = LinkedList()
sll1.head = Node("mon")
# create 2 other nodes
n2 = Node("tue")
n4 = Node("thu")
n3 = Node("wed")
n5 = Node("fri")
# link first node(head) to second node
sll1.head.next = n2
# link second node to third node
n2.next = n3
n3.next = n4
n4.next = n5
# sll1.insertNode("wed", 3)
print([node.val for node in sll1])
sll1.traverse()
print(sll1.countNodes())
print(sll1.searchNode("fri"))
# sll1.deleteNode(2)
# print([node.val for node in sll1])
