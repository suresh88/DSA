# 637. Average of Levels in Binary Tree

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC: O(n) and SC: O(n)
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        result = []    
        q = deque([root])

        while len(q) != 0:
            numnodes = len(q)
            temp = 0
            for _ in range(numnodes):
                node = q.popleft()
                temp = temp + node.val
                # this is for binary tree
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                
            result.append(temp/numnodes)

        return result