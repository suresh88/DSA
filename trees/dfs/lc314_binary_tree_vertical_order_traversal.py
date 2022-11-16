# 314. Binary Tree Vertical Order Traversal

'''
Medium:
--------
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = {}
        
        def dfs(node, x, y):
            # common to leaf and non-leaf nodes
            if x not in result:
                result[x] = {}
            if y not in result[x]:
                result[x][y] = [node.val]
            else:
                result[x][y].append(node.val)
            
            # no base case needed for leaf nodes
            # Recursive case: Internal nodes
            if node.left is not None:
                dfs(node.left, x-1, y+1)
            if node.right is not None:
                dfs(node.right, x+1, y+1)
                
        dfs(root, 0, 0)
        
        output = []
        for x in sorted(result.keys()):
            temp = []
            for y in sorted(result[x].keys()):
                temp.extend(result[x][y])
            output.append(temp)
        return output
