class Solution(object):
    def subsets(self, nums):
        res = []
        op = []
        solve(nums, 0, op, res)
        return res


def solve(nums, start, op, res):
    if start == len(nums):
        res.append(op[:])
        return
    solve(nums, start + 1, op, res)
    op.append(nums[start])
    solve(nums, start + 1, op, res)
    op.pop()
