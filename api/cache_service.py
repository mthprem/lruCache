from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove the least recently used item

        self.cache[key] = value

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            value = self.cache.pop(key)
            # Move the accessed item to the end to mark it as most recently used
            self.cache[key] = value
            return value

    def update_capacity(self, capacity):
        self.capacity = capacity

# # Example usage
# cache = LRUCache(3)  # Creating a cache with capacity 3
# cache.put('a', 1)
# cache.put('b', 2)
# cache.put('c', 3)
#
# print(cache.get('a'))  # Output: 1 (a is the most recently used item)
# print(cache.get('b'))  # Output: 2 (b is now the most recently used item)
# print(cache.get('d'))  # Output: None (d is not present in the cache)
#
# cache.update_capacity(2)  # Updating the capacity to 2
# cache.put('d', 4)  # Adding a new item which exceeds the capacity
# print(cache.get('c'))  # Output: None (c was removed due to exceeding capacity)
