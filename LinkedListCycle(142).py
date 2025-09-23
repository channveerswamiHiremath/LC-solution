# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        cycle = False
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        if cycle == False:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return fast
        