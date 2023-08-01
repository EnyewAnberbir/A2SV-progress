class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    a = 0
    b = int(sqrt(c))

    while a <= b:
      res = a * a + b * b
      if res == c:
        return True
      if res < c:
        a += 1
      else:
        b -= 1

    return False
