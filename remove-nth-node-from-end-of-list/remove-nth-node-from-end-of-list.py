# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head 
        first = head
        for i in range(n):
            first = first.next
        
        if not first:
            return head.next
        
        while first.next:
            first = first.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head