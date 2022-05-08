# Given a binary tree, return the level order traversal of its node values in (ie, from left to right, level by level).

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC: O(n) and SC: O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []    
        q = deque([root])

        while len(q) != 0:
            numnodes = len(q)
            temp = []
            for _ in range(numnodes):
                node = q.popleft()
                # this is for binary tree
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                temp.append(node.val)
            result.append(temp)

        return result