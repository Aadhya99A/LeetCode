# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head:
            reg = []
            curr = head
            while curr != None:
                reg.append(curr.val)
                curr = curr.next
            reg.sort()
            nhed = ListNode(reg[0])
            kirk = None
            for i in range(len(reg)):
                if i == 0:
                    kirk = nhed
                else:
                    kirk.next = ListNode(reg[i])
                    kirk = kirk.next
            return nhed
        else:
            return None