"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new_map = {None: None}

        curr = head

        while curr:
            new_node = Node(curr.val)
            old_to_new_map[curr] = new_node
            curr = curr.next
        
        curr = head

        while curr:
            copy = old_to_new_map[curr]
            copy.next = old_to_new_map[curr.next]
            copy.random = old_to_new_map[curr.random]
            curr = curr.next
        
        return old_to_new_map[head]
