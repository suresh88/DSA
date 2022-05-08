# 965. Univalued Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return []
    
        rootValue = root.val 
        q = deque([root])
    
        while len(q) != 0:
            numnodes = len(q)
            for _ in range(numnodes):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if node.val != rootValue:
                    return False
    
        return True