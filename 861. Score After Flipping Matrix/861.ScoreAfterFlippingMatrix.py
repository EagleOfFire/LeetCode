class Solution(object):
    def matrixScore(self,grid):
        for i in range(len(grid)):
            row = grid[i]
            if row[0] == 0:
                row = flip(row)

        for i in range(len(grid[0])):
            count0 = 0
            count1 = 0
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    count1 += 1
                else:
                    count0 += 1
            if count0 > count1:
                for j in range(len(grid)):
                    grid[j][i] = 1 - grid[j][i]
        result = 0
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                result += row[j] * (2 ** (len(row) - j-1))
        return result


def flip(row):
    for x in range(len(row)):
        row[x] = 1 - row[x]
    return row

