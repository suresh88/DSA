# 543. Diameter of Binary Tree

'''
Easy:
-----
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        diameter = [0]
        def dfs(node):
            # Base case: Leaf node
            if node.left is None and node.right is None:
                return 0
            
            # Recursive case: internal node
            ht = 0
            dia = 0
            if node.left is not None:
                lh = dfs(node.left)
                ht = max(ht, 1 + lh)
                dia += 1 + lh
                
            if node.right is not None:
                rh = dfs(node.right)
                ht = max(ht, 1 + rh)
                dia += 1 +rh
                
            diameter[0] = max(diameter[0], dia)
            return ht
            
        dfs(root)
        return diameter[0]