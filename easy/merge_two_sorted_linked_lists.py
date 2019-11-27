class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, l1 , l2):
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head=ListNode(0)
        current=head
        while l1 is not None and l2 is not None:
            if l1.val >= l2.val:
                current.next = l2.val
                l2 = l2.next
            else:
                current.next = l1.val
                l1 = l1.next
            current = current.next

            if l1 is not None:
                current.next = l1
            if l2 is Not None:
                current.next = l2
        return head.next
