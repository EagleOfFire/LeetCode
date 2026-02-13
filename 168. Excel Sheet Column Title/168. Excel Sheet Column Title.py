class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber != 0:
            if columnNumber % 26 == 0:
                ans += "Z"
                columnNumber = (columnNumber // 26) - 1
            else:
                ans += chr((columnNumber % 26) + 64)
                columnNumber = columnNumber // 26
        return ans[::-1]


sol = Solution()

print(sol.convertToTitle(1))
print(sol.convertToTitle(28))
print(sol.convertToTitle(701))
print(sol.convertToTitle(731))
