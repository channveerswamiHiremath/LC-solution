# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp = list1
        vals = []

        while temp:
            vals.append(temp.val)
            temp = temp.next

        temp = list2
        while temp:
            vals.append(temp.val)
            temp = temp.next

        vals.sort()

        list3 = ListNode()   
        temp = list3
        i = 0
        if len(vals) == 0:
            return
        while i < len(vals):
            temp.val = vals[i]
            if i != len(vals) - 1:   
                temp.next = ListNode()
                temp = temp.next
            i += 1
        return list3
        