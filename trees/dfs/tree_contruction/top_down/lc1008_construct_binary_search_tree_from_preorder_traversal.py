# 1008. Construct Binary Search Tree from Preorder Traversal
'''
Medium:
---------
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        inorder = sorted(preorder)
        
        ino_map = {} #Store the index of every number in the inorder traversal in a hashmap
        for i in range(len(inorder)):
            ino_map[inorder[i]] = i
            
        def helper(A1, start1, end1, A2, start2, end2):
            # return the subtree root of the binary tree constructed from the preorder subarray
            # A1[start1..end1] and inorder subarray A2[start2..end2]
            
            # Base case
            if start1 > end1:
                return None
            elif start1 == end1:
                return TreeNode(A1[start1])
            # At this point, we know that preorder list is more than 1 long
            
            # Recursive case
            # The first value is the root of the subtree
            rootval = A1[start1]
            # Find the index of this value in the inorder subarray
            # It is guaranteed to be present in the inorder subarray
            rootindex = ino_map[rootval]
            
            #Everything to its left is the left subtree. Everything to its right is the right subtree.
            numleft = rootindex - start2
            numright = end2 - rootindex
            subtreeroot = TreeNode(A1[start1])
            subtreeroot.left = helper(A1, start1 + 1, start1 + numleft, A2, start2, start2 + numleft - 1)
            subtreeroot.right = helper(A1, start1 + numleft + 1, start1 + numleft + numright, A2, rootindex + 1, rootindex + numright)
            
            return subtreeroot
        
        return helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)