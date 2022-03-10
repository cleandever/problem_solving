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
    def sol1(self, l1, l2):
        """
        시간복잡도 : O(N*N)
        """
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

    def sol2(self, l1, l2):
        """
        시간복잡도 : O(N)
        """
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            cur.next = ListNode()
            cur = cur.next
            n1, n2 = 0, 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next

            carry, remainder = divmod(n1 + n2 + carry, 10)
            cur.val = remainder

        return dummy.next


    def addTwoNumbers(self, l1, l2):
        #return self.sol1(l1, l2)
        return self.sol2(l1, l2)


l1 = trans_to_list([2, 4, 3])
l2 = trans_to_list([5, 6, 4])

sol = Solution()
head = sol.addTwoNumbers(l1, l2)
assert trans_to_arr(head) == [7, 0, 8]