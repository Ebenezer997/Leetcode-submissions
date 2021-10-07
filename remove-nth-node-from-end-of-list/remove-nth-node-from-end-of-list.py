# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #fast and slow pointers
        #two pointers one will go faster and reach the end and the other will follow after the other has reach  
        slow = head 
        fast = head
        #looping and first trip in terms of n
        for i in range(n):
            fast = fast.next
        # if fast does not exist we return the other value
        if not fast:
            return head.next
        #second trip
        while fast.next:
            #move the fast pointer followed by slow pointer
            fast = fast.next
            slow = slow.next
            #when the fast pointer reach the end
        #slow pointer is forwarded twice 
        slow.next = slow.next.next
        #return head
        return head