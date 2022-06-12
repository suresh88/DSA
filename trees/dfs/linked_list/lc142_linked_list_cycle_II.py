# 142. Linked List Cycle II
'''
Medium
--------
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        hare = tortoise = head
        while hare.next is not None and hare.next.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                third = head
                while tortoise != third:
                    third = third.next
                    tortoise = tortoise.next
                return third
        return None