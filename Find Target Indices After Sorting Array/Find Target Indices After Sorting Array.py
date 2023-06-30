class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if sortedNums[i] == target:
                ans.append(i)
        return ans
