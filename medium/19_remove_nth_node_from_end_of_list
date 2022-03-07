# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Goal: slow at dist(length-1-n)
        # Get fast to n+1, and keep slow.next to head so dist(fast,slow)=n+1
        # iterate until fast is at length, so that slow is at length-n-1
        fast = slow = start = ListNode(0, head)
        i = 0
        while i <= n:
            fast = fast.next
            i+=1

        while fast != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return start.next
