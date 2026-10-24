# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        carry = 0

        while l1 or l2 or carry:
            l1val, l2val = l1.val if l1 else 0, l2.val if l2 else 0

            new_node = ListNode((l1val + l2val + carry) % 10)
            carry = (l1val + l2val + carry) // 10
            curr.next = new_node
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head.next
