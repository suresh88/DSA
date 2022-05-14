# 226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        def dfs(node):
            oldleft = node.left
            oldright = node.right
            
            node.left = oldright
            node.right = oldleft
            
            if node.left is not None:
                dfs(node.left)
                
            if node.right is not None:
                dfs(node.right)
                
        dfs(root)
        return root