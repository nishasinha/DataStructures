"""
Collision
A hash function
- should be computable
- equally distribute keys

But it still might happen that many keys are mapped to one hash value.
This is called collision. To overcome:

1. Use Chaining
hash table here is an array, each index corresponds to a linked list.

adv:
- hash table can store any amount of data, used when we dont know how many entries may come up.

disadv:
- extra space taken.
- cache performance is bad, data stored in linked list.
- some keys in hash table may remain empty, other keys may have big liked list.

time:
load factor = alpha = m/n
where m is the number of keys
n is the number of slots.

search = O(1 + alpha)
insert = O(1)
delete = O(1 + alpha)


2. Open Addressing
Here whe collision happens, the next location in the hash table is searched for.
Given a number, location = h(number)
if that location is already filled, look for next location via:

* linear probing
next location = h(number + 1)
if occupied,
next location = h(number + 2)
....

h(number + i)
-> clustering may happen, a lot of keys maps to same index and it becomes time consuming to search for free place.
-> cache performance is good

* quadratic probing
next location = h(number + 1 * 1)
if occupied,
next location = h(number + 2 * 2)
...

h(number + i*i)
-> clustering chances are low

* double hashing
next location = (1 * h2(number)) mod n
if occupied,
next location = (2 * h2(number)) mod n
...

location = (h(number) + i * h2(number)) mod n
h1(number) = number mod n
h2(number) = prime - (number mod prime)

where prime is the smallest prime number before n.

-> clustering does not happen
-> cache performance is poor.
-> takes time to compute next hash function.

Now, to search also, use the same hash functions fr the next location.
To delete, search and remove the key from hash table and also mark that cell as "deleted", so that search does not stop.
time:
O(1 / (1-alpha))


3. Rehashing
load factor should be <= 0.75 to have O(1) time to search.

So, on every insert, this value must be checked and if the value goes beyond 0.75, rehash.
For Rehash, make a new array of double the previous size and make it the new bucketarray.
Then traverse to each element in the old bucketArray and call the insert() for each so as to insert it into the new
larger bucket array.

"""