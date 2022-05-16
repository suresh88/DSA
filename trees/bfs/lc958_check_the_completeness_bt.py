# 958. Check Completeness of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        expectedid = 1    
        q = deque([(root, 1)])

        while len(q) != 0:
            numnodes = len(q)
            for _ in range(numnodes):
                node, id = q.popleft()
                if id == expectedid:
                    expectedid +=1
                else:
                    return False
                if node.left is not None:
                    q.append((node.left, 2*id))
                if node.right is not None:
                    q.append((node.right, 2*id+1))
        return True