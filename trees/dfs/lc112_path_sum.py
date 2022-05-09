# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
        flag = [False]
        
        def dfs(node, target):
            target -= node.val
            # Base case: leaf node
            if node.left is None and node.right is None:
                if target == 0:
                    flag[0] = True

            # Recursive Case: Internal Node
            if node.left is not None:
                dfs(node.left, target)
            if node.right is not None:
                dfs(node.right, target)

        dfs(root, targetSum)
        return flag[0]