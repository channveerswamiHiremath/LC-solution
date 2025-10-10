# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1 = l1
        temp2 = l2
        total = []
        carry = 0
        while temp1 or temp2 or carry:
            v1 = temp1.val if temp1 else 0
            v2 = temp2.val if temp2 else 0
            ttl = v1 + v2 + carry
            carry = ttl // 10
            total.append(ttl % 10)
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

        list3 = ListNode()
        head = list3
        temp = list3
        
        for i in range(len(total)):
            temp.val = total[i]
            if i != len(total) - 1:
                temp.next = ListNode()
                temp = temp.next
        return head
