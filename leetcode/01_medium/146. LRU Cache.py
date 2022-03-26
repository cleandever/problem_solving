"""
https://leetcode.com/problems/lru-cache/
"""
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        value = self.cache.get(key, -1)
        if value == -1:
            return value
        del self.cache[key]
        self.cache[key] = value
        return value

    def put(self, key, value):
        # 이미 키가 있는 경우
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
            return

        if len(self.cache) >= self.capacity:
            del self.cache[next(iter(self.cache))]

        self.cache[key] = value

items = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
lru = LRUCache(items[0][0])
for item in items[1:]:
    if len(item) == 1:
        print(lru.get(item[0]))
    else:
        lru.put(item[0], item[1])



