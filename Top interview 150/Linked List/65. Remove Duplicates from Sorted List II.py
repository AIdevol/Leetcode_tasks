class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmpHead = ListNode(0)
        oked = tmpHead

        movH = head
        while movH:
            movT = movH
            while movT.next and movT.val == movT.next.val:
                movT = movT.next

            if movH == movT:
                oked.next = movH
                oked = movH
                movH = movH.next
            else:
                d1 = movH
                d2 = movH.next
                while d1 != movT:
                    del d1
                    d1 = d2
                    d2 = d2.next
                movH = movT.next
                del movT

        oked.next = None

        ret = tmpHead.next
        del tmpHead
        return ret
