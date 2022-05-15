# 156. Binary Tree Upside Down

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        The pointer changes can be made in a single step from top to bottom.
        Since the root to be returned is leaf at the bottom it seems that top down BFS should work.
        The global problem is to turn the tree upside down.
        Locally speaking, each node needs to redirect its right child pointer to point to its parent.
        (asuming parent information is available to it.)
        ... and to redirect its left pointer to point to its "right sibling" (in the original tree)
        (assuming its right sibling information is available to it.)
        This also means that when it inserts the left child into the queue, it will package that information            with it.
        '''
        
        if root is None:
            return None
        
        globalroot = None
        
        q = collections.deque([(root, None, None)])
        while len(q) != 0:
            (node, parent, rightsibling) = q.popleft()

            oldleft = node.left
            oldright = node.right
            node.left = rightsibling
            node.right = parent
            
            if oldleft is not None:
                q.append((oldleft, node, oldright))

        return node
            