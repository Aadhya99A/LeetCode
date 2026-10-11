# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heads = [heads for heads in lists]
        vals = []
        for i in heads:
            while i != None:
                vals.append(i.val)
                i = i.next
        vals.sort()
        head = None
        curr = None
        for i in range(len(vals)):
            if i == 0:
                head = ListNode(vals[0])
                curr = head
            else:
                curr.next = ListNode(vals[i])
                curr = curr.next
        return head