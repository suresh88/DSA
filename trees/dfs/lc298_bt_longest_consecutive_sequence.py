# 298. Binary Tree Longest Consecutive Sequence
'''
Medium:
-------
Given the root of a binary tree, return the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        globalans = [1]
        
        def dfs(node, pval, lengthsofar):
            if node.val - pval == 1:
                lengthsofar += 1
            else:
                lengthsofar = 1
            
            if lengthsofar > globalans[0]:
                globalans[0] = lengthsofar
            
            #Base case: Leaf Node
            if node.left is None and node.right is None:
                pass
                    
            if node.left is not None:
                dfs(node.left, node.val, lengthsofar)
            if node.right is not None:
                dfs(node.right, node.val, lengthsofar)
           
        dfs(root, root.val, [0])
        return globalans[0]