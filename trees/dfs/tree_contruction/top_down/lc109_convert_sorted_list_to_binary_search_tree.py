# 109. Convert Sorted List to Binary Search Tree
'''
Medium:
--------
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

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
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
            
        #At this point, the list has been copied to the nums array
        # T(n) = O(n) and S(n): O(n)
        def helper(A, start, end):
            if start > end:
                return None
            elif start == end:
                return TreeNode(A[start])
            else:
                mid = start + (end-start)//2
                subtreeroot = TreeNode(A[mid])
                subtreeroot.left = helper(A, start, mid-1)
                subtreeroot.right = helper(A, mid+1, end)
                
                return subtreeroot
            
        return helper(nums, 0, len(nums)-1)