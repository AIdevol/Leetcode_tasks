# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = None
        last = None
        i = 1
        t = list1
        while t is not None:
            if i == a:
                head = t
            if i == b + 1:
                last = t.next
                break
            t = t.next
            i += 1
        head.next = list2
        while head.next is not None:
            head = head.next
        head.next = last
        return list1
