"""
문제 URL : https://leetcode.com/problems/find-the-duplicate-number/
"""


class Solution:
    # sorting
    def sorting_solution(self, nums):
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return nums[i]

    # index
    def index_solution(self, nums):
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] *= -1
            if nums[idx] > 0:
                return abs(nums[i])
        return -1

    def findDuplicate(self, nums):
        # return self.sorting_solution(nums)
        return self.index_solution(nums)


sol = Solution()
assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2
assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3
