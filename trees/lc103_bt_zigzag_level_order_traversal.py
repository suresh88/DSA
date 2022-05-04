# Binary Tree Zigzag Level Order Traversal
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC: O(n) and SC: O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []    
        q = collections.deque([root])
        zigzag = True
        while len(q) != 0:
            numnodes = len(q)
            temp = collections.deque()
            for _ in range(numnodes):
                node = q.popleft()
                # this is for binary tree
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if not zigzag:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
            result.append(temp)
            zigzag = not zigzag

        return result