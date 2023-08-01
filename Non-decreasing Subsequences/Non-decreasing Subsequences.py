class Solution:
  def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(s: int, path: List[int]) -> None:
      if len(path) > 1:
        result.append(path)

      sets = set()

      for i in range(s, len(nums)):
        if nums[i] in sets:
          continue
        if not path or nums[i] >= path[-1]:
          sets.add(nums[i])
          dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result
