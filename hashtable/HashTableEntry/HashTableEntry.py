class HashTableEntry:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        self.__next = None
    
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, data):
        self.__key = data
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, data):
        self.__value = data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, entry):
        self.__next = entry

    @property
    def data(self):
        return {"key": self.key, "value": self.value}

    def delete(self):
        self.next_node = None

    def collapse(self):
        if self.next_node is None:
            return [self.data]
        return [self.data] + self.next_node.collapse()

    def find(self, key):
        if self.next_node is None and self.key != key:
            raise KeyError('List does not contain key')

        if self.key == key:
            return self.data
        
        return self.next_node.find(key)
        

    def __str__(self):
        return f'Key: {self.key}, Value: {self.value}'

    def __repr__(self):
        return f'HashTableEntry("{self.key}", "{self.value}")'

    def __eq__(self, value):
        return {"key": self.key, "value": self.value} == value
