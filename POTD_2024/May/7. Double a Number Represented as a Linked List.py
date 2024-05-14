# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        head = self.reverse_list(head)
        current = head
        carry = 0
        last = None
        
        while current is not None:
            doubled_value = current.val * 2 + carry
            current.val = doubled_value % 10
            carry = doubled_value // 10
            last = current
            current = current.next
        
        
        if carry > 0:
            last.next = ListNode(carry)
   
        head = self.reverse_list(head)
        
        return head
    
    def reverse_list(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    # Helper function to convert a list of digits to a linked list
    def list_to_linked_list(self, numbers):
        if not numbers:
            return None
        head = ListNode(numbers[0])
        current = head
        for num in numbers[1:]:
            current.next = ListNode(num)
            current = current.next
        return head

   
    def linked_list_to_list(self, head):
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        return result


