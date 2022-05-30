# 563. Binary Tree Tilt
'''
Easy:
-----
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.
'''
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