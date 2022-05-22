# 109. Convert Sorted List to Binary Search Tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #T(n): O(n)
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if head is None:
            return None
        
        # Find the length of the list
        length = 0
        p = head
        while p is not None:
            length += 1
            p = p.next
            
        # we know the length of the list at this point
        #Construct the BST from left to right: Left subtree, then root, then right subtree
        curr = [head]
        #curr[0] is pointing to very first node in inorder traversal.
        
        def helper(start, end):
            #Return value should be the root of the subtree, so that it can be connected as
            #...left or right child to its parent
            #Base case
            if start > end:
                return None
            if start == end:
                rootval = curr[0].val
                curr[0] = curr[0].next
                return TreeNode(rootval)
            
            # recursive case
            #start to mid-1 will make up the left subtree
            #mid will makeup the root
            #mid+1 to end will make up the right subtree
            mid = (start+end)//2
            leftsubtree = helper(start, mid - 1)
            r = TreeNode(curr[0].val)
            r.left = leftsubtree
            curr[0] = curr[0].next
            rightsubtree = helper(mid + 1, end)
            r.right = rightsubtree
            return r
        
        return helper(0, length-1)