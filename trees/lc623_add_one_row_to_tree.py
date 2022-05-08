# 623. Add One Row to Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root is None:
            return []
        
        if depth == 1:
            newnode = TreeNode(val)
            newnode.left = root
            root = newnode
                
        q = deque([root])
        d = 0
        while len(q) != 0:
            numnodes = len(q)
            d += 1
            for _ in range(numnodes):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if depth - 1 == d:
                    templeft = TreeNode(val)
                    tempright = TreeNode(val)
                    templeft.left = node.left
                    node.left = templeft
                    tempright.right = node.right
                    node.right = tempright

        return root