# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        nex = None
        if head == None:
            return 
        while curr != None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev
        