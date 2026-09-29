# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# no recursion, use a queue instead
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0

        while (size := len(queue)):
            for _ in range(size):
                node = queue.popleft()
                left, right = node.left, node.right
                
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            
            depth += 1

        return depth
