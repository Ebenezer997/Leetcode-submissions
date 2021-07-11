# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
       #create have three pointers 
       #head which iterate thru the list, Prev = hold pointers for previous node,(start from none),beginning of the linkedlist, Temp= temporary pointer to hold head while it moves.
        #prev will be set to none at the beginning of the linkedlist it begin  it
        #while head exist. we will set temp to head and we will move head. 
        #we will set temp.next to prev which reverse the pointer of the current node.
        #after reversing we will send prev to temp 
        #at last we will return prev.
        
        prev = None
        
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
      