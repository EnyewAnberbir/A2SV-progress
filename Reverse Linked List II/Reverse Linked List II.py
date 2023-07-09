# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        
        for _ in range(left - 1):
            pre = pre.next

        
        current = pre.next
        for _ in range(right - left):
            temp = pre.next
            pre.next = current.next
            current.next = current.next.next
            pre.next.next = temp

        return dummy.next
