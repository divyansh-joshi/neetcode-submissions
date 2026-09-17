# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            if root is None:
                return 0
            left_sum = max(rec(root.left), 0)
            right_sum = max(rec(root.right), 0)
            
            self.maxi = max(self.maxi, left_sum + right_sum + root.val)
            
            return root.val + max(left_sum, right_sum)
        self.maxi = -10**9
        rec(root)
        return self.maxi