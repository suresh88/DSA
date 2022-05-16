# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        Global problem: Determine if the Tree is BST
        Local (per-node) problem: Determine if the subtree at each node is a BST
        Local -> global: All local problems must return True for global solution to be True, 
        so if any local solution is False, global solution will become False.
        '''
        if root is None:
            return True
        
        isBST = [True]
        
        def dfs(node):
            '''
            A node will determine if it is BST by looking at its left and right subtrees
            The largest value in a left subtree should be smaller than the root value.
            The smallest value in the right subtree should be larger than the root value.
            Both subtrees should be BSTs.
            So each onde should return (smallest, largest, isbst) values in its subtree back to its parent.
            '''
            amibst = True
            smallest, largest = node.val, node.val
            
            if node.left is None and node.right is None:
                pass
            
            if node.left is not None:
                (s, l, b) = dfs(node.left)
                smallest = min(smallest, s)
                # largest = max(largest, l)
                if not b or l >= node.val:
                    amibst = False
                    
            if node.right is not None:
                (s, l, b) = dfs(node.right)
                # smallest = min(smallest, s)
                largest = max(largest, l)
                if not b or node.val >= s:
                    amibst = False
                    
            if amibst == False:
                isBST[0] = False
                
            return (smallest, largest, amibst)
        
        dfs(root)
        return isBST[0]