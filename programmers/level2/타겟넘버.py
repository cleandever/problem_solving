"""
https://programmers.co.kr/learn/courses/30/lessons/43165
"""
def solution(numbers, target):
    def recur(nums, remain_nums):
        if not remain_nums:
            if sum(nums) == target:
                return 1
            return 0
        else:
            return recur(nums + [remain_nums[0]], remain_nums[1:]) + \
                   recur(nums + [-remain_nums[0]], remain_nums[1:])

    return recur([], numbers)



assert solution([1,1,1,1,1], 3) == 5
assert solution([4, 1, 2, 1], 4) == 2