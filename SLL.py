class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node = node.next
    #Insertion
    def insertSLL(self,value,location):
        #create a new node first
        newNode = Node(value)
        #start insertion algorith
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                currNode = self.head
                index = 0
                #loop through the nodes except last as it will be covered in the above case
                while index < location-1:
                    currNode = currNode.next
                    index+=1
                #hold the next node physical location in variable nextNode
                nextNode = currNode.next
                currNode.next = newNode
                newNode.next = nextNode
                if currNode == self.tail:
                    self.tail = newNode
    #traversal 
    def traverseSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            currNode = self.head
            while currNode is not None:
                print(currNode.value)
                currNode = currNode.next
    #search
    def searchSLL(self,value):
        if self.head is None:
            print("The SLL does not exist")
        else:
            currNode = self.head
            while currNode is not None:
                if currNode.value == value:
                    return currNode.value
                    currNode=currNode.next
                else:
                    return "Value does not exist"
    #Delete a node 
    def deleteSLL(self,location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            #if removing the node from the first position
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            #if removing node from the last position
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        #break out of the loop if node.next is tail, means node is previous node
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                currNode = self.head
                index = 0
                #loop through the nodes except last as it will be covered in the above case
                while index < location-1:
                    currNode = currNode.next
                    index+=1
                #hold the next node physical location in variable nextNode
                nextNode = currNode.next
                currNode.next = nextNode.next
            
sll = SLL()
sll.insertSLL(400,0)
sll.insertSLL(400,0)
sll.insertSLL(400,0)
sll.insertSLL(400,0)
print(sll.searchSLL(400))
sll.deleteSLL(8)
sll.traverseSLL()
print([node.value for node in sll])
                

