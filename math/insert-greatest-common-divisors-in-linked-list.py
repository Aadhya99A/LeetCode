from math import gcd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lp = head
        rp = head.next
        while rp is not None:
            node = ListNode(gcd(lp.val, rp.val))
            node.next = rp
            lp.next = node
            lp = rp
            rp = rp.next
        return head