# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # so from p we want to go right
        # from q we want to go left
        # is this two pointers-esque?
        mi, ma = min(p.val, q.val), max(p.val, q.val)

        while not mi <= root.val <= ma:
            if root.val > ma:
                root = root.left
            elif root.val < mi:
                root = root.right
        
        return root