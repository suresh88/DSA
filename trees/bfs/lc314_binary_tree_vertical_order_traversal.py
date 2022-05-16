# 314. Binary Tree Vertical Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        pos = []
        neg = []
        zero = [[]]
        
        q = collections.deque([(root, 0)])
        while len(q) != 0:
            (node, x) = q.popleft()
            if x == 0:
                zero[0].append(node.val)
            if x > 0:
                if x > len(pos):
                    pos.append([])
                pos[x-1].append(node.val)
            if x < 0:
                if abs(x) > len(neg):
                    neg.append([])
                neg[abs(x)-1].append(node.val)
                
            if node.left is not None:
                q.append((node.left, x-1))
            if node.right is not None:
                q.append((node.right, x+1))
                
        neg = neg[::-1]
        neg.extend(zero)
        neg.extend(pos)
        
        return neg