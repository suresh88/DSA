# 662. Maximum width of a binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        result = []    
        q = deque([(root, 1)])

        while len(q) != 0:
            numnodes = len(q)
            temp = deque()
            first = None
            last = None
            for _ in range(numnodes):
                node, id = q.popleft()
                # this is for binary tree
                if node.left is not None:
                    q.append((node.left, 2*id))
                if node.right is not None:
                    q.append((node.right, 2*id+1))
                last = id
                if first is None:
                    first = id
            result.append(last-first+1)

        return max(result)