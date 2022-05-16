# 687. Longest Univalue Path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        '''
        Global problem: Find the longest unival path
        Local (per-node) problem: Find the longest inverted V-shaped unival path through each node.
        Local - > Global: Global solution will be maximum of all local solutions
        To compute the local solution, each node should know (from its left and right subtrees)...
        ... what is the length of the longest unival path from the root down to some leaf/ non-leaf
        This is the return value from each side to its parent.
        '''
        if root is None:
            return 0
        
        globalmax = [0]
        
        def dfs(node):
            mylongestVpath = 0
            mylongestpath = 0
            
            # Base case: Leaf node
            if node.left is None and node.right is None:
                pass
            
            # Recursive case: Internal node
            if node.left is not None:
                myleftpath = dfs(node.left)
                if node.val == node.left.val:
                    mylongestVpath = mylongestpath = 1 + myleftpath
                    
            if node.right is not None:
                myrightpath = dfs(node.right)
                if node.val == node.right.val:
                    mylongestpath = max(mylongestpath, 1 + myrightpath)
                    mylongestVpath += 1 + myrightpath 
                    
            if mylongestVpath > globalmax[0]:
                globalmax[0] = mylongestVpath
                
            return mylongestpath
                
        dfs(root)
        return globalmax[0]