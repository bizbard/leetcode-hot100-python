import collections
from typing import List, Optional

class DLinkedNode:
    def __init__(self, key=0, val=0, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        # 哈希表
        self.cache = {}
        # 双向链表
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.moveToHead(node)

        return node.val

    def put(self, key, val):
        if key not in self.cache:
            node = DLinkedNode(key, val)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1

            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1

        else:
            node = self.cache[key]
            node.val = val
            self.moveToHead(node)

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def removeNode(self, node):
        prev = node.prev
        next = node.next
        node.prev.next = next
        node.next.prev = prev


if __name__ == "__main__":
    # 双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。
    # 哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。
    # ======= Test Case =======
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    lRUCache.get(1)
    lRUCache.put(3, 3)
    lRUCache.get(2)
    lRUCache.put(4, 4)
    lRUCache.get(1)
    lRUCache.get(3)
    lRUCache.get(4)
    # ====== Driver Code ======