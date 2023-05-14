#question: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#solution 1: T.C: O(n) and S.C: O(n)
def isPalindrome(head):
        list=[]
        curr = head
        
        
        while curr:
            list.append(curr.val)
            curr = curr.next
            
        print(list)    
        return list == list[::-1]
# Solution 2: T.C: O(n) S.C: O(1) This is a combination of two other linked list problems (Reverse Linked List, Middle of the Linked List).

# Find the midpoint of the linked list using a slow pointer
# Reverse the 2nd half of the linked list (basically, reverse everything after the current position of the slow pointer).
# Simply, go through the reversed 2nd part of the linked list and check whether the values match up with the actual linked list.
# If they do, it's a palindrome. If they don't, it's not a palindrome.
 def isPalindrome(head):
        fast = slow = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        fast = head
        slow = self.reverseLinkedList(slow)
        
        while slow != None:
            if slow.val != fast.val:
                return False
                
            fast = fast.next
            slow = slow.next
        
        return True
        
def reverseLinkedList(self,head):
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev