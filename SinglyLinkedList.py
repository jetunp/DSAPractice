#Creation of singly linked list

class Node:
    #Fn to initalize the node data and reference to next node (currently both null)
    def __init__(self,data=None):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    #Fn to initialize head and tail
    def __init__(self):
        self.head = None
        self.tail = None
    #To make the linkedlist we create printable
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node = node.next
    #Insertion of nodes in singly linked list -At the beginning
    def push(self,new_data,location):
        new_node = Node(new_data)
        #check if empty
        if self.head==None:
            self.head = new_node
            self.tail = new_node
        else:
            #add node at the beginning
            if location == 0:
                new_node.next=self.head
                self.head=new_node
            #add element at the last
            elif location == -1:
                new_node.next= None
                self.tail.next = new_node
                self.tail = new_node
            #add element at any other place in linked list 
            else:
                #we need to loop through all the elements
                temp_node = self.head
                index = 0
                while index < location-1 :
                    #traversing through list everytime it will take value of the next node on the list
                    temp_node = temp_node.next
                    index += 1
                #by doing this we are inserting the new node between temp node and next node
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node
    #Traverse through singly linked list
    def traverse(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.data)
                node = node.next
    #search for a node in singly linked list
    def search(self,search_data):
        if self.head is None:
            print("Could not be in the SLL as SLL does not exist")
        else:
            node = self.head
            while node is not None:
                if node.data == search_data:
                    return node.data
                node = node.next
            return "The value does not exist in this LL"
    #Delete a node in the singly linked list
    def delete(self,location):
        if self.head is None:
            return "Linked List does not exist, nothing to delete"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None 
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None 
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location-1 :
                    #traversing through list everytime it will take value of the next node on the list
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
    # Delete the entire SLL
    def deleteEntire(self):
            if self.head is None:
                print("SLL does not exist")
            self.head = None
            self.tail = None
#create an object of the singly linked list
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(1,1)

print([node.data for node in singlyLinkedList])
singlyLinkedList.push(1,1)
print([node.data for node in singlyLinkedList])
# singlyLinkedList.traverse()
# singlyLinkedList.search(202330)
# singlyLinkedList.delete(4)
# print([node.data for node in singlyLinkedList])
# singlyLinkedList.deleteEntire()
# print([node.data for node in singlyLinkedList])