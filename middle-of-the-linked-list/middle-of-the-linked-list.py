# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
#         slow = fast = head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         if fast.next:
#             return slow.next
#         else:
#             return slow
        
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
        
        
        
        
        
        
		# slow=fast=head
		# while fast.next and fast.next.next:
		# 	slow=slow.next
		# 	fast=fast.next.next
		# if fast.next:
		# 	return slow.next
		# else:
		# 	return slow
        