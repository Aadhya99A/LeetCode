from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 0:
            return head
        plane = []
        curr = head
        while curr != None:
            plane.append(curr.val)
            curr= curr.next
        if plane:
            tru_rot = k%(len(plane))
        else:
            return None
        newk = deque(plane)
        newk.rotate(k)
        newk = list(newk)
        ret = None
        curt = None
        for i in range(len(newk)):
            if i == 0:
                ret = ListNode(newk[i])
                curt = ret
            else:
                curt.next = ListNode(newk[i])
                curt = curt.next
        return ret