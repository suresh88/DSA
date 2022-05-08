# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        level = 0
        while len(q) != 0:
            numnodes = len(q)
            level += 1
            for _ in range(numnodes):
                node = q.popleft()
                # this is for binary tree
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if node.left is None and node.right is None:
                    return level

