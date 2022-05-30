# 250. Count Univalue Subtrees
'''
Medium:
-------
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def dfs(node):
            # Base case: leaf node
            if node.left is None and node.right is None:
                return (1, True)
            
            # Recursive case: Internal node
            amiunival = True
            numunival = 0
            if node.left is not None:
                numleftunival, isleftunival = dfs(node.left)
                if not isleftunival or node.val != node.left.val:
                    amiunival = False
                numunival += numleftunival
                
            if node.right is not None:
                numrightunival, isrightunival = dfs(node.right)
                if not isrightunival or node.val != node.right.val:
                    amiunival = False
                numunival += numrightunival
            
            if amiunival:
                numunival += 1
                
            return numunival, amiunival            
        (total, boolean) = dfs(root)
        return total