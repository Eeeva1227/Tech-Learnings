# Redis

## What is Redis
Redis stands for **REmote DIctionary Server** and was written in C.

It is a NoSQL advanced key-value data store. The read and write operations are very fast in Redis because *it stores all data in memory*.

The data can also be stored on the **disk** and can be written back to the memory.

It is often referred to as a data structure server because keys can contain strings, hashes, lists, sets, sorted sets, bitmpas, and hyperloglogs.

Since Redis stores its data in memory, it is mostly commonly used as a cache.

# Redis Commands
 
## Redis Data Types
Redis is a key-value store.
Redis support different types of data structures as *values*. The *key* in Redis is a **binary-safe** string, with a max size of 512 MB, but you should always consider creating shorter keys.

A binary-safe string is a string that can contain any kind of data, e.g. a JPEC image or a serialized Java object.

- String
- List
The elements are stored in a linked list, and the elements are sorted on the basis of the insertion order.
The list should be stored in those cases where the order of insertion matters and where the write speed matters as compared to the read speed, e.g, storing logs.