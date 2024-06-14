class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return 0
        count = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i + 1]:
                count += nums[i]-nums[i+1]+1
                nums[i+1] = nums[i] + 1
        return count