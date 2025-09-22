# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 0
        temp = head
        while temp != None:
            count += 1
            temp = temp.next
        
        travers = count // 2
        temp = head
        for i in range(travers):
            temp = temp.next
        return temp                