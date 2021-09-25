# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #append list
        s = []
        head = current = ListNode(0)
        for i in range(len(lists)):
            while lists[i] != None:
                s.append(lists[i].val)
                lists[i] = lists[i].next
        s.sort()
        for i in range(len(s)):
            current.next = ListNode(s[i])
            current = current.next
        return head.next
        