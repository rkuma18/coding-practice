'''
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

'''
class MyHashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key):
        index = self._hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def contains(self, key):
        index = self._hash(key)
        return key in self.buckets[index]

    def remove(self, key):
        index = self._hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def show_table(self):
        print(" Hash Table:")
        print("-" * 30)
        for i, bucket in enumerate(self.buckets):
            values = " → ".join(str(x) for x in bucket) if bucket else "None"
            print(f"[{i}] → {values}")
        print("-" * 30)


s = MyHashSet()
for item in [15, 25, 35, 5, 12, 2]:
    s.add(item)

s.show_table()

