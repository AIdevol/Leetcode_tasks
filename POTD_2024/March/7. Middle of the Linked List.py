# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        tmp = head
        while tmp:
            count+=1
            tmp = tmp.next
            
        middle = count//2
        l = 0
        while l < middle:
            head = head.next
            l+=1
        return head