class Solution:
    def sortColors(self, nums: list[int]) -> None:
        merge_sort_in_place(nums)


def merge_sort_in_place(m, start=0, end=None):
    if end is None:
        end = len(m)

    # Base case. A list of zero or one elements is sorted, by definition.
    if end - start <= 1:
        return

    # Recursive case. First, divide the list into equal-sized sublists.
    mid = (start + end) // 2

    # Recursively sort both sublists.
    merge_sort_in_place(m, start, mid)
    merge_sort_in_place(m, mid, end)

    # Then merge the now-sorted sublists.
    merge_in_place(m, start, mid, end)


def merge_in_place(m, start, mid, end):
    left = m[start:mid]
    right = m[mid:end]

    i = 0
    j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            m[k] = left[i]
            i += 1
        else:
            m[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements of left, if there are any.
    while i < len(left):
        m[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements of right, if there are any.
    while j < len(right):
        m[k] = right[j]
        j += 1
        k += 1
