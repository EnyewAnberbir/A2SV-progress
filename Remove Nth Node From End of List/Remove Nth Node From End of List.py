class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    coll = []
    current = head

    while current:
      coll.append(current)
      current = current.next

    if n == len(coll):
      return head.next

    if n == 1:
      coll[-2].next = None
    else:
      coll[-n-1].next = coll[-n+1]

    return head
