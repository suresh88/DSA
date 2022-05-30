# 437. Path Sum III
'''
Medium:
-------
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        
        globalcount = [0]
        
        def dfs(node, target, slate):
            slate.append(node.val)
            internalsum = 0
            for i in range(len(slate)-1, -1, -1):
                internalsum += slate[i]
                if internalsum == target:
                    globalcount[0] += 1
                    
            if node.left is None and node.right is None:
                pass
            
            if node.left is not None:
                dfs(node.left, target, slate)
            if node.right is not None:
                dfs(node.right, target, slate)
                
            slate.pop()
            
        dfs(root, targetSum, [])
        return globalcount[0]