class Solution(object):
    def isValid(self, s):
        brackets = ['()', '{}', '[]']
        while any(x in s for x in brackets):
            for br in brackets:
                s = s.replace(br, '')
        return not s