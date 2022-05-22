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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # T(n): O(nlogn)
        def helper(h):
            if h is None:
                return None
            elif h.next is None:
                return TreeNode(h.val)
            else:
                fast = slow = h
                pslow = None
                while fast.next is not None and fast.next.next is not None:
                    fast = fast.next.next
                    pslow = slow
                    slow = slow.next
                
                # At this point, slow pointer is pointing to the midpoint of the list
                subtreeroot = TreeNode(slow.val)
                if pslow:
                    pslow.next = None
                    subtreeroot.left = helper(h)
                subtreeroot.right = helper(slow.next)
                return subtreeroot
        
        return helper(head)