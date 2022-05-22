# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # T(n): O(n)
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
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