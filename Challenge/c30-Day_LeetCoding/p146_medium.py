# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/


from collections import deque
from collections import OrderedDict


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache_size = capacity
#         self.queue = deque()
#         self.hash_map = dict()

#     def get(self, key: int) -> int:
#         if key not in self.hash_map:
#             return -1
#         else:
#             self.queue.remove(key)
#             self.queue.appendleft(key)
#             return self.hash_map[key]

#     def put(self, key: int, value: int) -> None:
#         if key not in self.hash_map:
#             if len(self.queue) == self.cache_size:
#                 pop_key = self.queue.pop()
#                 self.hash_map.pop(pop_key)
#                 self.queue.appendleft(key)
#                 self.hash_map[key] = value
#             else:
#                 self.queue.appendleft(key)
#                 self.hash_map[key] = value
#         else:
#             self.queue.remove(key)
#             self.queue.appendleft(key)
#             self.hash_map[key] = value


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value
        self.dict.move_to_end(key)
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)


if __name__ == '__main__':
    # 設定 cache 大小為 2
    lru_cache = LRUCache(2)

    lru_cache.put(2, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(2))
    lru_cache.put(1, 1)
    lru_cache.put(4, 1)
    print(lru_cache.get(2))
