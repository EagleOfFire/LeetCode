class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        CommonPrefix = ""
        flag = 0
        for j in range(len(min(strs, key=len))):
            for i in range(len(strs)):
                if (i + 1) < len(strs):
                    if strs[i][j] == strs[i + 1][j]:
                        flag = 1
                    else:
                        flag = 0
                        break
            if flag == 1:
                CommonPrefix += strs[0][j]
            else:
                break
        return CommonPrefix
