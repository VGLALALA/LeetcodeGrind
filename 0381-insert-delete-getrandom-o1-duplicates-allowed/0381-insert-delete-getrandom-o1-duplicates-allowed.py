import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        # List of all values for O(1) getRandom
        self.values = []
        # Map from value to set of indices in self.values
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        """Insert val into the collection.
        Returns True if val was not already present, False otherwise."""
        is_new = val not in self.indices or len(self.indices[val]) == 0
        self.values.append(val)
        self.indices[val].add(len(self.values) - 1)
        return is_new

    def remove(self, val: int) -> bool:
        """Remove one occurrence of val from the collection.
        Returns True if val was present, False otherwise."""
        if val not in self.indices or not self.indices[val]:
            return False
        # Remove an arbitrary index of val
        idx_to_remove = self.indices[val].pop()
        last_val = self.values[-1]
        last_idx = len(self.values) - 1

        # Move the last element into the spot of the removed element if needed
        if idx_to_remove != last_idx:
            self.values[idx_to_remove] = last_val
            # Update indices for last_val
            self.indices[last_val].remove(last_idx)
            self.indices[last_val].add(idx_to_remove)

        # Remove the last element from list
        self.values.pop()
        return True

    def getRandom(self) -> int:
        """Return a random element from the collection."""
        return random.choice(self.values)

