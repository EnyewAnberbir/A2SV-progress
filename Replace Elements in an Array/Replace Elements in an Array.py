class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_dict = {num: idx for idx, num in enumerate(nums)}
        for op in operations:
            idx = num_dict[op[0]]
            nums[idx] = op[1]
            num_dict.pop(op[0])
            num_dict[op[1]] = idx
        return nums
           
