"""
https://leetcode.com/problems/maximum-frequency-stack/
"""

# 시간초과발생
# from collections import defaultdict
# class FreqStack:
#     def __init__(self):
#         self.stack = []
#         self.counter = defaultdict(int)
#
#     def push(self, val):
#         self.stack.append(val)
#         self.counter[val] += 1
#
#     def pop(self):
#         sorted_counter = sorted(self.counter.items(), key=lambda x: x[1], reverse=True)
#         most_freq = sorted_counter[0][1]
#         most_freq_vals = [x[0] for x in list(filter(lambda x: x[1] == most_freq, sorted_counter))]
#
#         for i in range(len(self.stack)-1, -1, -1):
#             if self.stack[i] in most_freq_vals:
#                 self.counter[self.stack[i]] -= 1
#                 ret = self.stack.pop(i)
#                 break
#         return ret


import heapq as hq
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.counter = 0
        self.heap = []

    def push(self, val):
        self.freq[val] += 1

        # frequency가 크고 나중에 추가될 수록 우선순위가 높음
        hq.heappush(self.heap, (-self.freq[val], -self.counter, val))

        self.counter += 1

    def pop(self):
        val = hq.heappop(self.heap)[2]
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
for val in [5, 7, 5, 7, 4, 5]:
    obj.push(val)

assert obj.pop() == 5
assert obj.pop() == 7
assert obj.pop() == 5
assert obj.pop() == 4