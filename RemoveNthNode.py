class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n = 2
        # 1 -> 2 -> 3 -> 4 -> 5 -> NULL
        # L         R
        # Two PTR
        # L pointer is at begining
        # R pointer is shifted by n
        # until right pointer is at the end of the list ( R = NULL )
        # space between the pointers is equal to n in this case 2
        # continuously shift by 1
        # reassign the pointer to the next.next pointer to remove it
        # dummy node initialize before the head
        # dummy.next = head of og linked list
        # L pointer will be at 3 then we turn its next into 5 to create
        # 1 -> 2 -> 3 -> 5 -> NULL
        # return dummy.next to return og head which is 1

        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = head

        while n > 0 and right: # shift right n unites to the right
            right = right.next
            n-=1

        while right: # while right doesnt equal null
            left = left.next 
            right = right.next

        # delete 4
        left.next = left.next.next
        return dummy.next

# I finally learned how to properly use dummy nodes!
