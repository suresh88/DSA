# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Global Problem: Determine if the whole tree is height balanced
        local problem: Each node will determine whether it is height balanced
        local -> global: If each node is height balanced then the whole tree is height balanced
        To solve the local problem, each node needs to know the heights of its left and right subtrees.
        So each node will return its height to its parent.
        '''
        if root is None:
            return True
        
        globalbalance = [True]
        def dfs(node):
            
            myheight = 0
            amibalanced = True
            
            if node.left is None and node.right is None:
                pass
            
            leftheight, rightheight = 0, 0
            if node.left is not None:
                leftheight = 1 + dfs(node.left)
                
            if node.right is not None:
                rightheight = 1 + dfs(node.right)
                
            myheight = max(leftheight, rightheight)
            if abs(leftheight - rightheight) > 1:
                amibalanced = False
                globalbalance[0] = False
                
            return myheight
        
        dfs(root)
        return globalbalance[0]