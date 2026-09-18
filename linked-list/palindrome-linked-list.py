# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        eml = []
        curr = head
        while curr.next != None:
            eml.append(curr.val)
            curr = curr.next
        eml.append(curr.val)
        lp, rp = 0, len(eml) -1
        for i in range(len(eml)//2):
            if eml[lp] != eml[rp]:
                return False
            lp += 1
            rp -= 1
        return True