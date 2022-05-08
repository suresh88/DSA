# 1161. 1161. Maximum Level Sum of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        level = 0
        maxsum = float('-inf')
        minlevel = 0
        while len(q) != 0:
            numnodes = len(q)
            total = 0
            level += 1
            for _ in range(numnodes):
                node = q.popleft()
                # this is for binary tree
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                total += node.val
                
            if total > maxsum:
                maxsum = total
                minlevel = level
        
        return minlevel