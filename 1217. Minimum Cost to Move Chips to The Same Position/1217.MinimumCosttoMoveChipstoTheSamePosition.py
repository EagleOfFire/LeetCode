class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        pair = 0
        impair = 0
        for i in range(len(position)):
            if position[i] % 2:
                impair += 1
            else:
                pair += 1
        return min(pair, impair)


sol = Solution()

print(sol.minCostToMoveChips([1, 2, 3]))
print(sol.minCostToMoveChips([2, 2, 2, 3, 3]))
print(sol.minCostToMoveChips([1, 1000000000]))
