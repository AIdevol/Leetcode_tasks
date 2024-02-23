# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        l3 = ListNode(0)
        head = l3
        
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = l2
                l3 = l3.next
                l2 = l2.next
        
        while l1:
            l3.next = l1
            l3 = l3.next
            l1 = l1.next
        
        while l2:
            l3.next = l2
            l3 = l3.next
            l2 = l2.next
        
        return head.next
