"""
16.25 LRU Cache
Design and build a "least recently used" cache, which evicts the least recently
used item. The cache should map from keys to values (allowing you to insert
and retrieve a value associated with a particular key) and be initialized
with a max size. When it is full, if should evict the least recently used
item.
"""


class Cache:
    """LRU Cache"""
    def __init__(self, max_size):
        self.__max_size = 10
        self.__cache = {}
        self.__addOrder = []

    def addItem(self, key, value):
        # purge last used item from cache is size too large
        if self.isFull():
            self.purgeLast()
        if key in self.__cache:
            return -1
        self.__cache[key] = value
        self.__addOrder.append(key)

    def purgeLast(self):
        key = self.__addOrder.pop(0)
        del self.__cache[key]

    def getValue(self, key):
        return self.__cache[key]

    def isFull(self):
        return len(self.__addOrder) == self.max_size
