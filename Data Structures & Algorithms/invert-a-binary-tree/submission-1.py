# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if the root is None, we've recursed into a null child, and we keep it null
        if not root:
            return None
        
        # if it has no children, the inversion is just itself
        if root.left == root.right == None:
            return root
        
        # otherwise swap left and right and run recursively on it
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root