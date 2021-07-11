# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #have a temp head to hold the head
        #While head and head.next exist we swap succcesvive elements
        #after swapping you move the head to the next two positions and return the temp
        
        temp = head
        while head and head.next:
            head.val,head.next.val = head.next.val,head.val
            head = head.next.next
            
        return temp
    
        