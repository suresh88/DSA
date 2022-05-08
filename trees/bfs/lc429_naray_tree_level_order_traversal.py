# Given an n-ary tree, return the level order traversal of its nodes' values.

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# TC: O(n) and SC: O(n)
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                # this is for n-aray tree
                for child in node.children:
                    q.append(child)
                temp.append(node.val)
            result.append(temp)

        return result