# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
        Iteratively swap pointers
    '''

    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head

        # initial setup for iteration
        start = head.next
        prev = head
        head.next = None

        # iteratively swapping pointers of pairs
        while start is not None:
            tmp = start.next
            start.next = prev  # reverse pointer
            prev = start  # move forward
            start = tmp
        return prev
