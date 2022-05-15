# 156. Binary Tree Upside Down

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        The pointer changes can be made in a single step from top to bottom.
        Since the root to be returned is leaf at the bottom it seems that top down DFS should work.
        The global problem is to turn the tree upside down.
        Locally speaking, each node needs to redirect its right child pointer to point to its parent.
        (asuming parent information is available to it.)
        ... and to redirect its left pointer to point to its "right sibling" (in the original tree)
        (assuming its right sibling information is available to it.)
        This also means that when it calls dfs on its left child, it will pass that information down to it.
        '''
        
        if root is None:
            return None
        
        globalroot = [None]
        
        def dfs(node, parent, rightsibling):
            oldleft = node.left
            oldright = node.right
            node.left = rightsibling
            node.right = parent
            
            if oldleft is None and oldright is None:
                globalroot[0] = node
            
            if oldleft is not None:
                dfs(oldleft, node, oldright)
                
        dfs(root, None, None)
        return globalroot[0]
            