# 94. Binary Tree Inorder Traversal
'''
Easy:
------
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        stack = [(root, None)]
        while len(stack) != 0:
            (node, zone) = stack[-1]
            if zone is None:
                stack[-1] = (node, 'arrival')
                if node.left is not None:
                    stack.append((node.left, None))
                    
            elif zone == 'arrival':
                stack[-1] = (node, 'interim')
                result.append(node.val)
                if node.right is not None:
                    stack.append((node.right, None))
                    
            elif zone == 'interim':
                stack[-1] = (node, 'departure')
                stack.pop()
                
        return result