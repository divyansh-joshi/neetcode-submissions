# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p != None and q is None or p is None and q != None:
            return False
        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right  

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def rec(root, subRoot):
            if root is None and subRoot is not None:
                return False

            if root.val == subRoot.val:
                if self.isSameTree(root, subRoot) == True:
                    return True
            
            return rec(root.left, subRoot) or rec(root.right, subRoot)
        return rec(root, subRoot)
