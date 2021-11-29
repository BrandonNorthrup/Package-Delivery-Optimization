# Brandon Northrup
# Student ID: 001177877


class HashMap:
    # Constructor
    # O(1) complexity
    def __init__(self, starting_cap=10):
        # Initialize the hash map with 10 buckets
        self.map = []
        for i in range(starting_cap):
            self.map.append([])

    # Creates a hash map key
    # O(1) complexity
    def create_key(self, key):
        bucket = int(key) % len(self.map)
        return bucket

    # Gets a value from the hash map
    # O(N) complexity
    def get_hash_value(self, key):
        key_hash = self.create_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Inserts a value into the hash map for each package
    # O(N) complexity
    def insert(self, key, value):
        hash_key = self.create_key(key)
        key_value = [key, value]
        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value])
            return True
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[hash_key].append(key_value)
            return True

    # Updates keys as necessary, and provides an error if the key is missing
    # O(N) complexity
    def update(self, key, value):
        key_hash = self.create_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('Error with key: ' + key)

    # Removes a value from the hash table when called
    # O(N) complexity
    def delete(self, key):
        key_hash = self.create_key(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
