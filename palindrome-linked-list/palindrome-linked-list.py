# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
#         fast = head
#         slow = head
        
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
        
#         prev = None
#         while slow:
#             temp = slow.next
#             slow.next = prev
#             prev = slow
#             slow = temp
        
#         left,right = head,prev
        
#         while right:
#             if left.val != right.val:
#                 return False
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next
        if fast:
            slow = slow.next
        while slow and slow.val == prev.val:
            slow, prev = slow.next, prev.next
        return not slow