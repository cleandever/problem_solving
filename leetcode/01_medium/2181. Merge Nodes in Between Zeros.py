"""
https://leetcode.com/problems/merge-nodes-in-between-zeros/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head):
        cur = head.next
        cur_sum = 0

        res = []
        while cur:
            if cur.val == 0:
                res.append(cur_sum)
                cur_sum = 0
            else:
                cur_sum += cur.val
            cur = cur.next

        return array_to_list(res)


def array_to_list(nums):
    head = None
    for n in nums:
        node = ListNode(n)
        if head is None:
            head = node
            prev = head
        else:
            prev.next = node
            prev = node
    return head


if __name__ == '__main__':
    nums = [0, 3, 1, 0, 4, 5, 2, 0]
    head = array_to_list(nums)

    sol = Solution()
    res = sol.mergeNodes(head)
    assert res.val == 4
    assert res.next.val == 11
