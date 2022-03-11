"""
https://leetcode.com/problems/rotate-list/
"""
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
    def rotateRight(self, head, k):
        if not head:
            return head

        q = []
        cur = head
        while cur:
            q.append(cur)
            cur = cur.next

        k = k % len(q)
        if k == 0:
            return head

        dummy = ListNode(0)
        dummy.next = q[len(q) - k]

        cur = dummy
        for i in range(len(q) - k, len(q)):
            cur.next = q[i]
            cur = cur.next

        for i in range(len(q) - k):
            cur.next = q[i]
            cur = cur.next
        cur.next = None

        return dummy.next


sol = Solution()

nums = [1, 2, 3, 4, 5]
k = 2
head = trans_to_list(nums)
ret = sol.rotateRight(head, k)
assert trans_to_arr(ret) == [4, 5, 1, 2, 3]

nums = [1, 2]
k = 1
head = trans_to_list(nums)
ret = sol.rotateRight(head, k)
assert trans_to_arr(ret) == [2, 1]
