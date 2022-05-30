# 513. Find Bottom Left Tree Value
'''
Medium:
--------
Given the root of a binary tree, return the leftmost value in the last row of the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        leftmost = [] # maintain the leftmost node in each level
        
        
        def dfs(node, parentdepth):
            '''
            I need to know my own depth, so that I'm the first node to be visited at that depth...
            I should be added to the leftmost array. I know I am the leftmost in my level if the leftmost array
            isn't long enough to have accomodated any node at my depth.
            '''
            mydepth = parentdepth + 1
            if mydepth > len(leftmost):
                leftmost.append(node.val)
            
            # Base case: Leaf node
            if node.left is None and node.right is None:
                pass
            
            # Recursive case: Internal node
            if node.left is not None:
                dfs(node.left, mydepth)
            if node.right is not None:
                dfs(node.right, mydepth)
                
        dfs(root, 0)
        return leftmost[-1]