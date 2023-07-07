class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1,0,-1):
            for j in range(len(nums)-1):
                if i != j:
                     if target-nums[j]== nums[i]:
                        return [i,j] 
                        break
