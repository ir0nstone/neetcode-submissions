# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        level = 0
        
        to_pop = 1
        next_level = 0

        levels = []

        curr = []
        while queue:
            for _ in range(to_pop):
                node = queue.popleft()
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                    next_level += 1
                if node.right:
                    queue.append(node.right)
                    next_level += 1

            levels.append(curr)
            curr = []

            level += 1
            to_pop = next_level
            next_level = 0
        
        return levels