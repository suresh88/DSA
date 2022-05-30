# 449. Serialize and Deserialize BST
'''
Medium:
--------
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ""
        
        # Use preorder serialization
        result = []
        def helper(node):
            result.append(str(node.val))
            if node.left is not None:
                helper(node.left)
            if node.right is not None:
                helper(node.right)
                
        helper(root)
        return ",".join(result)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None
        
        splitdata = data.split(",")
        preorder = [int(i) for i in splitdata]
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
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans