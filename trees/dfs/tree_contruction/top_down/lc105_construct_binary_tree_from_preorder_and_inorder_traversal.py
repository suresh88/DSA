# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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
            