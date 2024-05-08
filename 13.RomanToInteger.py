class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        thisdict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        i = 0
        while i < len(s):
            if (i + 1) < len(s):
                if s[i] + s[i + 1] == "IV":
                    result += 4
                    i += 2
                elif s[i] + s[i + 1] == "IX":
                    result += 9
                    i += 2
                elif s[i] + s[i + 1] == "XL":
                    result += 40
                    i += 2
                elif s[i] + s[i + 1] == "XC":
                    result += 90
                    i += 2
                elif s[i] + s[i + 1] == "CD":
                    result += 400
                    i += 2
                elif s[i] + s[i + 1] == "CM":
                    result += 900
                    i += 2
                else:
                    result += thisdict[s[i]]
                    i += 1
            else:
                result += thisdict[s[i]]
                i += 1
        return result

