# 987. Vertical Order Traversal of a Binary Tree

'''
Hard:
------
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                temp.extend(sorted(result[x][y]))
            output.append(temp)
        return output