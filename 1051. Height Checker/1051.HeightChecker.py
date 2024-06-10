class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        ans = 0
        expectedHeights = []
        expectedHeights[:] = heights[:]
        expectedHeights.sort()
        if expectedHeights == heights:
            return 0
        for i in range(len(heights)):
            if heights[i] != expectedHeights[i]:
                ans += 1
        return ans