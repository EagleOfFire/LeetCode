class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i > 0 :
                    diff = grid[i - 1][j] - grid[i][j]
                    if diff >= 0:
                        ans += diff+1
                        grid[i][j] += diff+1
        return ans


sol = Solution()

print(sol.minimumOperations([[3,2],[1,3],[3,4],[0,1]]))
print(sol.minimumOperations([[3,2,1],[2,1,0],[1,2,3]]))