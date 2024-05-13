class Solution(object):
    def isPalindrome(self, x):
        list1 = list(str(x))
        list2 = list(str(x))
        list2.reverse()
        if list1 == list2:
            return True
        else:
            return False
