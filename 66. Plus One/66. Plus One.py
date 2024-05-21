class Solution(object):
    def plusOne(self, digits):
        integer = ""
        r = []
        for digit in digits:
            integer += str(digit)
        result = list(str(int(integer) + 1))
        for digit in result:
            r.append(int(digit))
        return r