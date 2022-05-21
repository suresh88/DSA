# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                if node.right is not None:
                    stack.append((node.right, None))
                    
            elif zone == 'interim':
                stack[-1] = (node, 'departure')
                result.append(node.val)
                stack.pop()
                
        return result