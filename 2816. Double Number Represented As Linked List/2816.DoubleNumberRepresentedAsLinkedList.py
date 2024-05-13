# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        value1 = []
        actuallist = head
        while actuallist.next is not None:
            value1.append(actuallist.val)
            actuallist = actuallist.next
        value1.append(actuallist.val)

        value1 = ''.join(str(e) for e in value1)
        result = list(str(int(value1) * 2))
        result.reverse()
        LN = None
        for i in range(len(result)):
            LN = ListNode(result[i], LN)
        return LN
