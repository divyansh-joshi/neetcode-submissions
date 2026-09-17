# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root, mini, maxi):
            if root == None:
                return True
            if root and root.val >= maxi or root.val <= mini:
                return False
            return rec(root.left, mini, root.val) and rec(root.right, root.val, maxi)
        return rec(root, -math.inf, math.inf)