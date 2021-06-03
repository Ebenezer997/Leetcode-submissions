# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        f = head
        while f and f.next:
            if f.next.val==val:
                f.next=f.next.next
            else : 
                f=f.next
        return head.next if head.val==val else head
       
       