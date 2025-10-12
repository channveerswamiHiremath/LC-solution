# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dup = []
        temp = head
        while temp :
            dup.append(temp.val)
            temp = temp.next
        count = 0
        if len(dup) != 0:
            dup[count] = dup[0]
        else:
            return
        i = 1
        while i < len(dup):
            if dup[i] != dup[count]:
                count += 1
                dup[count] = dup[i]
            i += 1
        dup = dup[:count + 1]
        new = ListNode()
        temp = new
        i = 0
        while i < len(dup):
            temp.val = dup[i]
            if i != len(dup) - 1:
                temp.next = ListNode()
                temp = temp.next
            i += 1
        return new
