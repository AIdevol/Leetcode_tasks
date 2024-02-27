# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)  # Dummy node for nodes less than x
        greater_dummy = ListNode(0)  # Dummy node for nodes greater than or equal to x
        less_ptr = less_dummy
        greater_ptr = greater_dummy

        while head:
            if head.val < x:
                less_ptr.next = head
                less_ptr = less_ptr.next
            else:
                greater_ptr.next = head
                greater_ptr = greater_ptr.next
            head = head.next
        
        greater_ptr.next = None  # Set the end of the greater partition
        less_ptr.next = greater_dummy.next  # Connect the two partitions

        return less_dummy.next

