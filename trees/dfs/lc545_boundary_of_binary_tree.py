# 545. Boundary of Binary Tree

'''
Medium:
-------
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.
'''

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