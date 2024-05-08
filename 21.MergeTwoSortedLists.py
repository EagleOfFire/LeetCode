class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    value1 = []
    value2 = []
    actuallist = list1
    if list1 == []:
        return list2
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
    return value1


list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
print(mergeTwoLists(list1, list2))
list1 = []
list2 = []
print(mergeTwoLists(list1, list2))
list1 = []
list2 = ListNode(0, None)
print(mergeTwoLists(list1, list2))
