# 515. Find Largest Value in Each Tree Row


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []    
        q = deque([root])

        while len(q) != 0:
            numnodes = len(q)
            largest = float('-inf')
            for _ in range(numnodes):
                node = q.popleft()
                largest = max(largest, node.val)
                # this is for binary tree
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                
            result.append(largest)

        return result