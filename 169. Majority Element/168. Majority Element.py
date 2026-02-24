class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ans = 0
        thisdict = {}
        for i in range(len(nums)):
            if str(nums[i]) in thisdict:
                thisdict[str(nums[i])] = thisdict[str(nums[i])] + 1
            else:
                thisdict[str(nums[i])] = 1
        print(thisdict)
        for x in thisdict:
            if str(ans) in thisdict :
                if int(thisdict[x]) > int(thisdict[str(ans)]):
                    ans = int(x)
            else:
                ans = int(x)
        return ans


Sol = Solution()

#print(Sol.majorityElement([3,2,3]))
print(Sol.majorityElement([2,2,1,1,1,2,2]))
#print(Sol.majorityElement([3,3,4]))