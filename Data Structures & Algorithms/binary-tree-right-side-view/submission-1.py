# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = {}
        def rec(root, level):
            if root == None:
                return

            if level not in self.answer:
                self.answer[level]= root.val
            
            if root.right != None:
                rec(root.right, level + 1)
            if root.left != None:
                rec(root.left, level + 1)
        rec(root, 0)
        ans = []
        for key in sorted(self.answer):
            ans.append(self.answer[key])
        return ans