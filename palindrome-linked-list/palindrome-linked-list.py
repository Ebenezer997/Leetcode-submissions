# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        number = []
        while head != None:
            number.append(head.val)
            head = head.next
        if number == number[::-1]:
            return True
        return False
        
#         full_number = []
#         while head != None:
#             full_number.append(head.val)
# 		    head = head.next
# 		if full_number == full_number[::-1]:
#             return True
# 		return False
        

