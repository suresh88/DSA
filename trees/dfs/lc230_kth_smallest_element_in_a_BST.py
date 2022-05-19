# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Root is not null
        kth = [0]
        
        def dfs(node, numpred, k):
            # Base case: Leaf Node
            if node.left is None and node.right is None:
                numpred += 1
                if numpred == k:
                    kth[0] = node.val
                return numpred
            
            # Recursive Case: internal Node
            if node.left is not None:
                numpred = dfs(node.left, numpred, k)
                
            numpred += 1
            if numpred == k:
                kth[0] = node.val
                
            if node.right is not None:
                numpred = dfs(node.right, numpred, k)
                
            return numpred
        
        dfs(root, 0, k)
        return kth[0]