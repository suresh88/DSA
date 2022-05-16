# 545. Boundary of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
        
        leftboundary = [root.val]
        if root.left is not None:
            
            curr = root.left
            while curr is not None:
                leftboundary.append(curr.val)
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr = curr.right
                
            leftboundary.pop()
        
        rightboundary = []
        curr = root
        if root.right is not None:
            
            curr = root.right
            while curr is not None:
                rightboundary.append(curr.val)
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr = curr.left
                
            rightboundary.pop()
        rightboundary.reverse()
        
        leaves = []
        def dfs(node):
            if node.left is None and node.right is None:
                leaves.append(node.val)

            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
                
        dfs(root)
        
        return leftboundary + leaves + rightboundary