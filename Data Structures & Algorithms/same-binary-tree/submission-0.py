# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = [p]
        q_stack = [q]

        while p_stack:
            p_val = p_stack.pop()
            q_val = q_stack.pop()

            if not p_val and not q_val:
                continue
            elif not p_val or not q_val:
                return False
            elif p_val.val != q_val.val:
                return False
            
            p_stack.append(p_val.left)
            p_stack.append(p_val.right)
            q_stack.append(q_val.left)
            q_stack.append(q_val.right)
        
        return not q_stack
