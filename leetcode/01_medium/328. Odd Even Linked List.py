"""
https://leetcode.com/problems/odd-even-linked-list/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head:
            return head

        odd = head
        even = head.next
        even_temp = head.next

        while odd and odd.next:
            odd.next = odd.next.next
            if odd.next is None:
                break

            odd = odd.next
            even.next = odd.next
            even = even.next


        odd.next = even_temp
        return head



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

sol = Solution()
sol.oddEvenList(node1)
