# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        heights = {None: 0}
        stack = [root]

        while stack:
            node = stack[-1]

            if node.left not in heights:
                stack.append(node.left)
            elif node.right not in heights:
                stack.append(node.right)
            else:
                node = stack.pop()
                
                if abs(heights[node.left] - heights[node.right]) > 1:
                    return False
                
                heights[node] = 1 + max(heights[node.left], heights[node.right])

        return True