#Time Complexity : O(1) for all operations
#Space Complexity : O(n) where n is the number of unique elements stored in the hashset
class MyHashSet:

    def __init__(self):
        # Initializing  an empty set to store unique elements
        self.hashset = set()

    def add(self, key: int) -> None:
        # Adding the key to the hashset.
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        # Removing the key from the hashset if it exists
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        # Checking if the key exists in the hashset
        return key in self.hashset

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
