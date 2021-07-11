# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        odd = head
        even = head.next
        evenhead = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenhead
        return head
#         head2 = head
#         head = head.next
#         while head and head.next:
#             head.val, head.next.val = head.next.val, head.val
#             head = head.next.next.next
            
#         return head2
        