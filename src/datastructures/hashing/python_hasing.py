"""
Hashing in Python

In Python hashing is supported via dictionaries.

- Dictionaries use array based open addressing, with random probing.

when dict is started, it has 8 slots in array.
the first element is inserted at hash(key).
and keeps on.
Each entry in table is <hash value, key, value>

as the first collision happens,
python checks the key and value, if match, does not do nothing.
if key or value does not match, it inserts at next location by random probing.

load faction 2/3, and rehashing happens at that point.

"""


class Hash:
    def __init__(self):
        self.hash_table = {}

    def insert(self, key, value):
        self.hash_table[key] = value

    def delete(self, key):
        del self.hash_table[key]

    def print_hash(self):
        for k,v in self.hash_table.items():
            print("{}: {}".format(k, v))


if __name__ == '__main__':
    print("********** Hashing *************")
    hash_table = Hash()
    for i in range(1, 100):
        hash_table.insert(str(i), i)

    hash_table.print_hash()
