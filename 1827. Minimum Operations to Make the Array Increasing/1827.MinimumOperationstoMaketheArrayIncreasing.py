def minOperations(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0
    count = 0
    for i in range(len(nums)-1):
        if nums[i] >= nums[i + 1]:
            count += nums[i]-nums[i+1]+1
            nums[i+1] = nums[i] + 1
    return count


#print(minOperations([1, 1, 1]))
print(minOperations([1, 5, 2, 4, 1]))
