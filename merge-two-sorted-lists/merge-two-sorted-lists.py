# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #if list 2 is empty return list 1 and inverse too
        if not l2 : return l1
        if not l1 : return l2
        # Assign dummy(temporay) head to  and also asign it to current.
        dummy = ListNode()
        current = dummy
        
        #while list1 and list2 exist: if the current value in list1 is less than list 2 
        #the next pointer is assigned to them
        while l1 and l2:
            if l1.val < l2.val:
                #the next pointer is assigned to them
                current.next = l1
                #update the pointer to the next value in  list1
                l1 = l1.next
                #otherwise
            else:
                current.next = l2
                l2 = l2.next
            #after comparing the current pointer is updated
            current = current.next
            current.next = l1 or l2
        # if l1:
        #     current.next = l1
        # elif l2:
        #     current.next = l2
        
              
        return dummy.next
        
        
        
       