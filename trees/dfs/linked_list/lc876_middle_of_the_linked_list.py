# 876. Middle of the Linked List
'''
Easy:
------
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare = head
        tortoise = head
        
        while hare.next is not None and hare.next.next is not None:
            hare = hare.next.next
            tortoise = tortoise.next
            
        if hare.next is not None:
            tortoise = tortoise.next
            
        return tortoise