# 113. Path Sum II
'''
Medium:
-------
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        result= []
        
        def dfs(node, target, slate):
            target -= node.val
            slate.append(node.val)
            
            #Base case: Leaf Node
            if node.left is None and node.right is None:
                if target == 0:
                    result.append(slate[:])
                    
            if node.left is not None:
                dfs(node.left, target, slate)
            if node.right is not None:
                dfs(node.right, target, slate)
           
            slate.pop()
        dfs(root, targetSum, [])
        return result
            