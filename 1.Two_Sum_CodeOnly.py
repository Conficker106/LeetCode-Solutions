class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if j != i :
                    if nums[i] + nums[j] == target :
                        sol = [i,j]
                        return sol
