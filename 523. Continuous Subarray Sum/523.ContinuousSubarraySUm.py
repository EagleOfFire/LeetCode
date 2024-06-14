class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        mod_dict = {0: -1}
        cumulative_sum = 0

        for i in range(len(nums)):
            cumulative_sum += nums[i]
            mod = cumulative_sum % k

            if mod in mod_dict:
                if i - mod_dict[mod] > 1:
                    return True
            else:
                mod_dict[mod] = i

        return False