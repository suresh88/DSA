# 333. Largest BST Subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        globalsize = [0]
        
        def dfs(node):
            
            mysize = 1
            amibst = True
            mysmallest, mylargest = node.val, node.val
            
            if node.left is None and node.right is None:
                pass
            
            if node.left is not None:
                (size, smallest, largest, isbst) = dfs(node.left)
                mysize += size
                mysmallest = min(mysmallest, smallest)
                # mylargest = max(mylargest, largest)
                if not isbst or largest >= node.val:
                    amibst = False
                    
            if node.right is not None:
                (size, smallest, largest, isbst) = dfs(node.right)
                mysize += size
                # mysmallest = min(mysmallest, smallest)
                mylargest = max(mylargest, largest)
                if not isbst or node.val >= smallest:
                    amibst = False
                    
            if amibst and mysize > globalsize[0]:
                globalsize[0] = mysize
                
            return (mysize, mysmallest, mylargest, amibst)
        
        dfs(root)
        return globalsize[0]
