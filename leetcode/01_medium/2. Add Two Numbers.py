"""
https://leetcode.com/problems/add-two-numbers/
"""
from itertools import zip_longest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 리스트노드를 array 자료구조로 변환
def trans_to_arr(head):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums


# array를 리스트노드로 변환
def trans_to_list(nums):
    dummy = cur = ListNode(0)
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        nums1 = trans_to_arr(l1)
        nums2 = trans_to_arr(l2)

        # 두 수 더하기 연산
        res = []
        carry = 0
        for n1, n2 in zip_longest(nums1, nums2, fillvalue=0):
            carry, remainder = divmod(n1 + n2 + carry, 10)
            res.append(remainder)
        if carry == 1:
            res.append(1)

        return trans_to_list(res)


l1 = trans_to_list([2, 4, 3])
l2 = trans_to_list([5, 6, 4])

sol = Solution()
head = sol.addTwoNumbers(l1, l2)
assert trans_to_arr(head) == [7, 0, 8]