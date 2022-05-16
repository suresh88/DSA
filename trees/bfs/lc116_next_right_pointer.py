# 116. Populating Next Right Pointers in Each Node

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        q = deque([root])

        while len(q) != 0:
            numnodes = len(q)
            prevnode = None
            for _ in range(numnodes):
                node = q.popleft()
                # this is for binary tree
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if prevnode is not None:
                    prevnode.next = node
                prevnode = node

        return root