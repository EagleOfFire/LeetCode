from collections import defaultdict


class Solution:
    def beautifulSubsets(self,nums: list[int], k: int) -> int:
        mp = defaultdict(int)
        result = dfs(nums, 0 , k, mp)
        return result - 1


def dfs(nums:list[int], idx:int,k:int,mp:list[int])->int:
    if idx == len(nums):
        return 1
    taken = 0
    if mp[nums[idx]-k] == 0 and mp[nums[idx]+k]==0:
        mp[nums[idx]] +=1
        taken = dfs(nums, idx+1, k,mp)
        mp[nums[idx]] -= 1
    notTaken = dfs(nums,idx+1,k,mp)
    return taken + notTaken

