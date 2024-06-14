class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = nums1[:m]
        nums2 = nums2[:n]
        for item in nums2:
            nums.append(item)
        nums.sort()
        nums1[:] = nums[:]