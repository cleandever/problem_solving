"""
https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
"""
class Solution:
    def countPairs(self, nums, k):
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    count += 1
        return count


sol = Solution()

nums = [3,1,2,2,2,1,3]
k = 2
assert sol.countPairs(nums, k) == 4

nums = [1,2,3,4]
k = 1
assert sol.countPairs(nums, k) == 0