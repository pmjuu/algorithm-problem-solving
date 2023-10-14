# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (root == None):
            return True
        
        def getHeight(node) -> int:
            if (node == None):
                return 0
            
            return max(getHeight(node.left), getHeight(node.right)) + 1
        
        diff = abs(getHeight(root.left) - getHeight(root.right))
            
        if (diff <= 1):
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False