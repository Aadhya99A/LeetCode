# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2
        ret1, ret2, curr = None, None, None
        eml = []
        while c1 != None:
            eml.append(c1.val)
            c1 = c1.next
        while c2 != None:
            eml.append(c2.val)
            c2 = c2.next
        eml.sort()
        head = None
        curr = None
        for i in range(len(eml)):
            if i == 0:
                head = ListNode(eml[i])
                curr = head
            else:
                new_curr = ListNode(eml[i])
                curr.next = new_curr
                curr = new_curr
        return head
                