# 426. Convert Binary Search Tree to Sorted Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Global Problem: convert whole tree into sorted doubly linked list.
        Local Problem: Each node connect itself to its predecessor/ successor.
        It suffices if each node forms the connections with its predecessor only.
        It needs information about who its predecessor is.
        Where will that information come from? It could come from its left child (if it has one)... or from some ancestor above (if it doesn't have a left child)
        This is neither top-down or bottom-up. It is "in-order".
        It also needs to pass on information about itself to its successor.
        The successor would be in the right subtree (it it has one) or some ancestor (if it doesn't have right child). So, it would need to pass that information either down or up.
        '''
        if root is None:
            return None
        
        '''
        If each node is connected to predecessor, what is the first node going to be connected to?
        And how how will the list become circular?
        Answer: We will start with a sentinel node as the head. While the linear chain is completed, we will take first node and connect it to the last to complete the circle.
        '''
        
        sentinel = Node('dummy')
        def dfs(node, pred):
            
            # Base Case: Leaf Node
            if node.left is None and node.right is None:
                pred.right = node
                node.left = pred
                return node
            
            # Recursive Case: Internal Node
            if node.left is not None:
                pred = dfs(node.left, pred)
            
            pred.right = node
            node.left = pred
            pred = node
            
            if node.right is not None:
                pred = dfs(node.right, pred)
                
            return pred
        
        tail = dfs(root, sentinel)
        head = sentinel.right
        head.left = tail
        tail.right = head
        
        return head