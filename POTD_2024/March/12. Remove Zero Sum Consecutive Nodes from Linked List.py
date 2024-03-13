# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)

        dummy.next = head

        prefix_sum = 0

        seen = {0: dummy}

        # First pass: calculate prefix sums and store nodes in a dictionary

        while head:

            prefix_sum += head.val

            seen[prefix_sum] = head

            head = head.next

        # Second pass: traverse the list again and remove zero-sum sequences

        head = dummy

        prefix_sum = 0

        while head:

            prefix_sum += head.val

            head.next = seen[prefix_sum].next

            head = head.next

        return dummy.next



        
        






   



       







  

 








        