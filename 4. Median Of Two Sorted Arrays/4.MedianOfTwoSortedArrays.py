class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for i in range(len(nums2)):
            nums1.append(nums2[i])

        data = sorted(nums1)
        n = len(data)
        if n % 2 == 1:
            return data[n // 2]
        else:
            i = n // 2
            return (data[i - 1] + data[i]) / 2.0
