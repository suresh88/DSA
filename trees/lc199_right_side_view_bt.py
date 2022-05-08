# 199. Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []    
        q = deque([root])

        while len(q) != 0:
            numnodes = len(q)
            rightmost = None
            for _ in range(numnodes):
                node = q.popleft()
                rightmost = node.val
                # this is for binary tree
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                
            result.append(rightmost)

        return result