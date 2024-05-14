class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
     
        if not head or not head.next:
            return head

        stack = []
        current = head
        max_val = float('-inf')

     
        while current:
           
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next

        
        if not stack:
            return None
        
       
        head = stack[0]
        current = head
        for node in stack[1:]:
            current.next = node
            current = node
        current.next = None  

        return head


def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

