class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res =[]
        for i in nums:
            count =0
            for j in range(len(nums)):
                if i > nums[j]:
                    count += 1
            res.append(count)
        return res
