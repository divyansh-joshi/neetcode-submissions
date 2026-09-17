# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.answer = 0
        def rec(root, greatest):
            if root == None:
                return None
            
            if root.val >= greatest:
                self.answer += 1
                greatest = root.val
            
            rec(root.left, greatest)
            rec(root.right, greatest)
        rec(root, -1000)
        return self.answer