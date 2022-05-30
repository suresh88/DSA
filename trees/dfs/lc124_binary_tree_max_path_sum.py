# 124. Binary Tree Maximum Path Sum
'''
Hard:
------
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # the tree is given to be non-empty, so we don't need to check if the root is None
        
        # Global problem: Find the maximum path sum in the tree
        # Local (per-node) problem: Find the maximum path sum for an inverted V path through every node
        # Local -> Global: global solution will be the maximum of all local solutions
        # To calculate the local solution, each node will need the following information from its subtrees:
        # What is the maxpathsum of a path starting at the root of the subtree and going down to same leaf/non-leaf
        globalmax = [float('-inf')]
        
        def dfs(node): # returns the max path sum of a root to descendant path in the subtree rooted at node.
            mymaxpathsum = node.val
            mymaxVpathsum = node.val
            
            # Base case: leaf node
            if node.left is None and node.right is None:
                pass
            
            # Recursive case: Internal node
            if node.left is not None:
                leftmax = dfs(node.left)
                mymaxpathsum = mymaxVpathsum = max(mymaxpathsum, node.val + leftmax)
                
            if node.right is not None:
                rightmax = dfs(node.right)
                mymaxpathsum = max(mymaxpathsum, node.val + rightmax)
                mymaxVpathsum = max(mymaxVpathsum, node.val + rightmax, mymaxVpathsum + rightmax)
                
            if mymaxVpathsum > globalmax[0]:
                globalmax[0] = mymaxVpathsum
            return mymaxpathsum
        
        dfs(root)
        return globalmax[0]
                