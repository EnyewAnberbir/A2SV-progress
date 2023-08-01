class Solution:
  def partitionLabels(self, s: str) -> List[int]:
    result = []
    func = {c: i for i, c in enumerate(s)}

    a = 0
    b = 0

    for i, c in enumerate(s):
      b = max(b, func[c])
      if i == b:
        result.append(b - a + 1)
        a = b + 1

    return result
