# 993. Cousins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return []
        
        q = deque([root])
        
        while len(q) != 0:
            numnodes = len(q)
            px = None
            py = None
            for _ in range(numnodes):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                    if node.left.val == x:
                        px = node.val
                    if node.left.val == y:
                        py = node.val
                if node.right is not None:
                    q.append(node.right)
                    if node.right.val == x:
                        px = node.val
                    if node.right.val == y:
                        py = node.val
                if px is not None and py is not None:
                    return px != py

        return False