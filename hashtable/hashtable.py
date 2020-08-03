from HashTableEntry.HashTableEntry import HashTableEntry
from HashTableLinkedList.HashTableLinkedList import HashTableLinkedList
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=8):
        # Your code here
        self.__store = [None] * capacity
        self.__capacity = capacity
        self.__count = 0
        self.__min_capacity = 8

    @property
    def store(self):
        return self.__store

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, capacity: int):
        if type(capacity) is not int:
            raise ValueError(f'Capacity with value {capacity} is not type int')
            
        if capacity < self.__min_capacity:
            raise ValueError(f'Capacity with value {capacity} is less than {min_capacity}')

        self.__capacity = capacity

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count += value

        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            self.resize(self.capacity * 2)
        if load_factor < 0.2 and self.capacity > self.__min_capacity:
            self.resize(self.capacity // 2)

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # this is so useless
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity

    def fnv1(self, key: str, prime=2**40+2**8+0xb3, offset=14695981039346656037):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hashed_data = offset
        data_to_hash = key.encode()

        for byte in data_to_hash:
            hashed_data ^= byte
            hashed_data *= prime

        return hashed_data


    # def djb2(self, key):
    #     """
    #     DJB2 hash, 32-bit

    #     Implement this, and/or FNV-1.
    #     """
    #     # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value, count=1):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.store[index] is None:
            self.store[index] = HashTableLinkedList()

        # lets try to find the entry in the list
        existing_entry = self.store[index].find(key)
        entry = existing_entry or {"key": key, "value": value}
        if existing_entry:
            entry['value'] = value
        self.store[index].shift(entry)
        self.count = 0 if existing_entry else count



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.store[index] is None:
            print("Key not found")
            return
        
        entry_exists = self.store[index].find(key) # either None or a Data object
        if entry_exists:
            self.count = -1
            return self.store[index].delete(key)

        # otherwise
        return None
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.store[index] is None:
            return None
        data = self.store[index].find(key)
        return data['value'] if data else data  # either None type or data


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        entries = []

        for lists in self.store:
            if lists:
                entries.extend(lists.collapse())

        self.__store = [None] * self.capacity
        for entry in entries:
            self.put(**entry, count=0)
        


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
