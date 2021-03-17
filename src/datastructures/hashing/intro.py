"""
Hashing - an improvement over the direct access tables.

Consider the problem is to
- store phone numbers with other data as a record
- search record given phone number
- delete the record given phone number

Now, which data structure to use here:
1. Array - each phone number at one location

search, insert, delete - O(n)
search - O(Log n) if array is sorted.

2. Linked list of phone numbers and records.
O(n) - search, delete

3. Balanced Binary search tree with phone number as key.
search - O(Log n)
insert, delete - O(Log n)

4. Direct access table
A big array with phone number as index.
search, insert, delete - O(1)

space: O(m * 10^n), m is record size, n is number of digits in the phone number
Hence, not efficient. Also, that big integer is not supported by any programming language.

* Hashing - an improvement over Direct Access Table
- store data in an array.
- use a hash function to map the phone number to a smaller array index

* Hash Function
map a given integer or string to a smaller integer.
- should be efficiently computable.
- should uniformly distribute keys.
eg: (x % 10)

* Hash Table
an array where index is hashed value of keys, data is kept as pointer at given index.

* Collision
Since hashing maps keys to smaller index, it might happen that a new key may map to an already used index, called
collision.
To solve:
1. Chaining - one index maps linked list of values.
2. Open Addressing - all data in one table only, if the first index is occupied look for next address in row.


Trivial Hashing examples:
1. Given a list of numbers, find out if the a given element exists?
If the numbers in list are big, use hashing.
n = len(list)
hash table = arr[n]
h(x) = x mod n

Given a number, store it at hash_table[ h(number) ]
Search, at hash_table[ h(number) ]

2. Hashing for negative numbers
Lets say data is from -MAX to MAX.

n = MAX
hash_table = arr[MAX+1][2]
h(x) = x mod n

if x is >= 0, mark hash_table[x][0] = 1.
if x is <0, mark has_table[x][1] = 1.
"""