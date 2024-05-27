class Solution:
    def specialArray(self, nums: list[int]) -> int:
        result = -1
        length = len(nums)
        for i in range(length):
            X = i + 1
            count = 0
            for j in nums:
                if j >= X:
                    count = count + 1
            if count == X:
                result = X
        return result
