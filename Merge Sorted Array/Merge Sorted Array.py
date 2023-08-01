class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    a = m - 1     
    b = n - 1      
    c = m + n - 1  
    while b >= 0:
      if a >= 0 and nums1[a] > nums2[b]:
        nums1[c] = nums1[a]
        c -= 1
        a -= 1
      else:
        nums1[c] = nums2[b]
        c -= 1
        b -= 1
