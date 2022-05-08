# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = deque([(root, root)])

        while len(queue) != 0:
            numnodes = len(queue)
            for _ in range(numnodes):
                nodeL, nodeR = queue.popleft()
                if nodeL.val != nodeR.val:
                    return False
                if nodeL.left is not None and nodeR.right is not None:
                    queue.append((nodeL.left, nodeR.right))
                elif nodeL.left is not None or nodeR.right is not None:
                    return False
                
                if nodeL.right is not None and nodeR.left is not None:
                    queue.append((nodeL.right, nodeR.left))
                elif nodeL.right is not None or nodeR.left is not None:
                    return False
        return True