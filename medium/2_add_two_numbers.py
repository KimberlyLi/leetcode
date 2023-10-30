# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        currNode = result
        tens_place = carry = 0
        while l1 or l2 or carry:
            sum = carry
            sum = sum + l1.val if l1 else sum
            sum = sum + l2.val if l2 else sum
            carry, currNode.val = divmod(sum, 10)
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            if l1 or l2 or carry:
                currNode.next = ListNode()
                currNode = currNode.next
        return result