# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        eml = []
        curr = head
        while curr != None:
            eml.append(curr.val)
            curr = curr.next
        twins = []
        lp, rp = 0, len(eml) - 1
        while lp <= rp:
            twins.append(eml[lp] + eml[rp])
            rp -= 1
            lp += 1
        return max(twins)