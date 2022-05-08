# 559. Maximum Depth of N-ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
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
                for child in node.children:
                    q.append(child)
        return level