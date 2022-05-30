# 114. Flatten Binary Tree to Linked List
'''
Medium:
-------
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        sentinel = TreeNode("dummy")
        def dfs(node, pred):
            pred.left = node
            pred = node
            
            if node.left is not None:
                pred = dfs(node.left, pred)
                
            if node.right is not None:
                pred = dfs(node.right, pred)
                
            return pred
        
        dfs(root, sentinel)
        head = sentinel.left
        curr = head
        while curr is not None:
            curr.right = curr.left
            curr.left = None
            curr = curr.right
        return head