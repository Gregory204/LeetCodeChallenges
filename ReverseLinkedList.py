'''
Given the head of a singly linked list, reverse the list,
and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''

def ReverseLinkedList(head):
    prev = None
    curr = head
    while curr != None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev  # return new head D

'''
Old Linked List:
a -> b -> c -> d -> NULL
a = head, d = tail

New Linked List:
Null <- a <- b <- c <- d
or 
d -> c -> b -> a -> NULL
d = head, a = tail

'''
