"""
Hashmap that does closed addressing (chaining) to resolve hash collisions.
"""


class HashMapNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashMap:
    def __init__(self, size):
        """
        Construct a hash map and initialize any internals.

        @type size: int
        @param size: the size of the hashmap
        """
        self.max_size = size
        self.current_size = 0
        self._store = [None] * max_size

    def _hash(self, key):
        return hash(key) % self.max_size

    def set(self, key, val):
        """
        Set a value in the hash map

        @type key: str
        @param key: the key to use in finding the location
            of the value

        @type val: any
        @param val: the value to set

        @rtype: bool
        @returns: True if successful, otherwise False
        """
        index = self._hash(key)
        # found a list already
        if self._store[index]:
            pass
        # first at the index
        else:
            chain = LinkedList()
            self._store[index] = chain
            chain.append(val)

    def get(self, key, val):
        """
        Get the value stored under the key

        @type key: str
        @param key: the key to use in finding the location
            of the value

        @rtype: any
        @returns: the value stored at the key
        """
        pass

    def delete(self, key):
        """
        Delete the value stored at the key

        @type key: str
        @param key: the key to use in finding the location
            of the value

        @rtype: any
        @returns: The value deleted if successful, otherwise
            None
        """
        pass

    def load(self):
        """
        Get the load factor (items in hash map)/(size of hash map)

        @rtype: float
        @returns: the load factor
        """
        return self.current_size / self.max_size
