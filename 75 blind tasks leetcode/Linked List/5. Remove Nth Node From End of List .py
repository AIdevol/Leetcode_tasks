class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = d =head
        c=0
        while p!=None:
            c+=1
            if c>n+1:
                d=d.next
            p=p.next
        if c==n:
            return head.next
        d.next = d.next.next
        return head