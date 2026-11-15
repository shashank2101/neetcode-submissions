# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty or has only one node without a cycle
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        # Traverse until fast reaches the end of the list
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            if slow == fast:          # They met, so there is a cycle
                return True
                
        # If the loop finishes, fast hit a None pointer (no cycle)
        return False