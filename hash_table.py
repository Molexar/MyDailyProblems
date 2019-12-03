class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        if string[1]:
            hash_value = 0
            hash_value += ord(string[0]) * 100 + ord(string[1])
        if hash_value != 0:
            if self.table[hash_value]:
                self.table[hash_value].append(string)
            else:
                self.table[hash_value] = [string]
            return 0
        return 1

    def lookup(self, string):
        if string[1]:
            hash_value = 0
            hash_value += ord(string[0]) * 100 + ord(string[1])
        if hash_value != 0:
            if hash_value < 10000:
                if self.table[hash_value]:
                    if string in self.table[hash_value]:
                        return hash_value
        return -1

    def calculate_hash_value(self, string):
        if string[1]:
            hash_value = 0
            hash_value += ord(string[0]) * 100 + ord(string[1])
            return hash_value
        return -1


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))