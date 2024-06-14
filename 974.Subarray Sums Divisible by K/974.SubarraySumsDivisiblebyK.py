class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        mod, result = 0, 0
        mod_dict = dict()
        mod_dict[0] = 1

        for num in nums:
            mod = (mod + num)% k
            result += mod_dict.setdefault(mod, 0)
            mod_dict[mod] += 1


        return result 