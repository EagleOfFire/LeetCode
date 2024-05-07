# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value1 = []
        value2 = []
        n1 = ""
        n2 = ""
        actuallist = l1
        while actuallist.next is not None:
            value1.append(actuallist.val)
            actuallist = actuallist.next
        value1.append(actuallist.val)
        value1.reverse()
        actuallist = l2
        while actuallist.next is not None:
            value2.append(actuallist.val)
            actuallist = actuallist.next
        value2.append(actuallist.val)
        value2.reverse()

        value1 = ''.join(str(e) for e in value1)
        value2 = ''.join(str(e) for e in value2)
        result = list(str(int(value1) + int(value2)))
        LN = None
        for i in range(len(result)):
            LN = ListNode(result[i], LN)
        return LN
