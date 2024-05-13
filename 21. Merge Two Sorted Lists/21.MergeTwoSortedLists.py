# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        value1 = []
        value2 = []
        actuallist = list1
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        while actuallist.next is not None:
            value1.append(actuallist.val)
            actuallist = actuallist.next
        value1.append(actuallist.val)
        actuallist = list2
        while actuallist.next is not None:
            value2.append(actuallist.val)
            actuallist = actuallist.next
        value2.append(actuallist.val)
        for i in range(len(value2)):
            value1.append(value2[i])
        value1.sort()

        result = ListNode(value1[len(value1) - 1], None)
        for i in range(len(value1) - 2, -1, -1):
            result = ListNode(value1[i], result)
        return result
