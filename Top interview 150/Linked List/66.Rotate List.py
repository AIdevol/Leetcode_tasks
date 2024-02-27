# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        tail.next = head
        k %= length        
        new_tail_idx = length - k
        new_tail = head
        for _ in range(new_tail_idx - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head