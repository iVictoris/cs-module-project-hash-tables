from HashTableEntry.HashTableEntry import HashTableEntry

class HashTableLinkedList:
    def __init__(self):
        self.head: None | HashTableEntry = None
        self.tail: None | HashTableEntry = None
        self.size = 0

    def __len__(self):
        return self.size

    """
    Takes in a data object that has at least a key
    and value attribute and inserts to the front/head of the list
    """
    def shift(self, data) -> None:
        # if not hasattr(data, 'key') or not hasattr(data, 'value'):
        #     raise TypeError('data object does not contain either a key or value attribute')

        entry = HashTableEntry(**data)
        self.size += 1

        if self.head is None:
            self.head = entry
            self.tail = entry
        else:
            entry.next_node = self.head
            self.head = entry


    def unshift(self):
        if self.head is None:
            return None

        entry: HashTableEntry = self.head
        self.size -= 1

        if self.head is self.tail:
            self.head = None
            self.tail = None
            return entry.data
        
        if self.head.next_node is self.tail:
            self.head = self.tail
            return entry.data
        
        self.head = self.head.next_node
        entry.next_node = None

        return entry.data

    def print_list(self):
        if not self.head:
            return

        string_builder = ""
        entry = self.head

        while entry:
            string_builder += f"[key: {entry.key} value: {entry.value}] -> "
            entry = entry.next_node
        string_builder += "None"

        print(string_builder)

        
    """
    Method collapses the Linked List and returns an array of dicts containing key/value pairs
    """
    def collapse(self):
        if not self.head:
            return None
        entries = self.head.collapse()
        self.head = None
        self.size = 0
        return entries

    """
    Given a key, delete that node from the linked list and return it
    """
    def delete(self, key):
        previous, current = self.head, self.head
        if current.key == key:
            return self.unshift()

        current = current.next_node
        while current:
            if current.key == key:
                if current is self.tail:
                    self.tail = previous
                previous.next_node = current.next_node
                self.size -= 1
                return current.data
            previous = current
            current = current.next_node
        
        # when we exit the while loop, the item with the key was not found
        raise KeyError(f'Key {key} does not exist at this location in the linked list')
        
    def find(self, key):
        if self.head is None:
            return None

        if self.head.key == key:
            return self.head.data
        
        if self.head.key == key:
            return self.tail.data

        try:
            return self.head.find(key)
        except KeyError:
            return None

