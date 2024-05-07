class Solution(object):
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        for value in nums:
            for x in range(len(nums) - 1):
                x = x + 1
                if (value + nums[x] == target) and a != x:
                    return [a, x]
            a += 1
