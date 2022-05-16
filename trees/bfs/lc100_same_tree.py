# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        queue = deque([(p, q)])

        while len(queue) != 0:
            numnodes = len(queue)
            for _ in range(numnodes):
                nodep, nodeq = queue.popleft()
                if nodep.val != nodeq.val:
                    return False
                if nodep.left is not None and nodeq.left is not None:
                    queue.append((nodep.left, nodeq.left))
                elif nodep.left is not None or nodeq.left is not None:
                    return False
                if nodep.right is not None and nodeq.right is not None:
                    queue.append((nodep.right, nodeq.right))
                elif nodep.right is not None or nodeq.right is not None:
                    return False
        return True