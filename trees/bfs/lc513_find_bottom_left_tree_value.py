# 513. Find Bottom Left Tree Value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        result = None    
        q = deque([root])

        while len(q) != 0:
            numnodes = len(q)
            firstvalue = None
            for _ in range(numnodes):
                node = q.popleft()
                if firstvalue is None:
                    firstvalue = node.val
                # this is for binary tree
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                
            result = firstvalue

        return result