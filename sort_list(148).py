# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        vals = []
        while temp:
            vals.append(temp.val)
            temp = temp.next
        vals.sort()
        temp = head
        for i in range(len(vals)):
            temp.val = vals[i]
            temp = temp.next
        return head
