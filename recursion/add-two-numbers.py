# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        n1 = []
        n2 = []
        c1, c2 = l1, l2
        while c1 != None:
            n1.append(str(c1.val))
            c1 = c1.next
        while c2 != None:
            n2.append(str(c2.val))
            c2 = c2.next
        n1str = "".join(reversed(n1))
        n2str = "".join(reversed(n2))
        final = str(int(n1str) + int(n2str))
        flip = str(final[::-1])
        head = None
        curr = None
        for i in range(len(flip)):
            if i == 0:
                head = ListNode(int(flip[i]))
                curr = head
            else:
                curr.next = ListNode(int(flip[i]))
                curr = curr.next
        return head