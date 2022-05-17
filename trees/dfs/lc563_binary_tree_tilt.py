# 563. Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        # Bottom-up DFS
        # Global Problem: Tilt of the whole tree
        # Local problem: Calculate tilt of an individual node
        # Local -> Global: Global solution is summation of all local solutions
        # To solve local problem, each node needs (from its child) the sum of all node values in the child subtree
        # This will also be the return value
        
        globaltilt = [0]
        
        def dfs(node):
            
            if node.left is None and node.right is None:
                return node.val
            
            leftsum, rightsum = 0, 0
            if node.left is not None:
                leftsum = dfs(node.left)
                
            
            if node.right is not None:
                rightsum = dfs(node.right)
                
            mytilt = abs(leftsum - rightsum)
            mysum = node.val + leftsum + rightsum
            globaltilt[0] += mytilt
            
            return mysum
        
        dfs(root)
        return globaltilt[0]