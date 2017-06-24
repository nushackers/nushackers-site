---
author: ymichael
author_link: http://ymichael.com
categories:
- Digest
comments: true
date: 2015-08-26T00:00:00Z
title: 'Digest: Consistent Hashing'
url: /2015/08/26/digest-consistent-hashing/
---

_This is our first digest article. What's a digest article? Basically we source around NUS and write something that's technically interesting. [Let us know](/contact/) if you would like to submit an article!_

If you've ever taken a Data Structures course or written a sufficiently complex program, you probably know what a [Hash Table][] is.

## Some background
> In computing, a hash table (also hash map) is a data structure used to implement an associative array, a structure that can map keys to values. -Wikipedia

The key idea behind a Hash Table is the computation of an index using a __hash function__ to determine which 'bucket' or 'slot' to insert the given value.

Assuming we choose a fairly good hash function, and have sufficiently large number of slots, we are able to map each key to a unique bucket _(less collisions)_ and therefore achieve an __`O(1)`__ constant cost per operation (`get`, `set`).

When the __load__ on the hash table gets above a certain threshold, we do a __`resize operation`__.

> Resizing is accompanied by a full or incremental table rehash whereby existing items are mapped to new bucket locations. -Wikipedia

_If we choose when to resize carefully, this still leaves us with [amortized][] constant time operations._

## The problem
Imagine you decide to design and implement caching layer on top of you extremely popular application. You decide that a __hash table__ is a perfect data structure to implement this [cache][].

You start caching various thing and your application is now _blazing_ fast. Your cache size starts to grow and you resize your cache. Remember, each time you resize the cache, you need to re-hash all the existing keys and remap them to a larger number of buckets.

__What happens when you can't fit your entire cache on a single machine?__

2 machines! A distributed hash table ([DHT][])!

## Keyspace partitioning
If you've been following along, the question you should have right now, is __how do you resize a DHT across machines?__

If you think about it, if you had say, a million key-value pairs distributed across 5 machines, and now wanted to add 2 more machines (i.e. grow the hash table), resizing and rehashing all of them seems like a bad idea and probably a last resort.

> While running collections of caching machines some limitations are experienced. A common way of load balancing n cache machines is to put object o in cache machine number `hash(o) mod n`. But this will not work if a cache machine is added or removed because `n` changes and every object is hashed to a new location. -Wikipedia

## [Consistent Hashing][] to the rescue!

The key benefit of consistent hashing is that we can avoid rehashing every object when a new machine is added. The way we can visualize this, is via a circle and some modulo arithmetic.

0. Say for instance, we __randomly scatter each machine on the circle__ (perhaps by hashing its IP address, or some unique identifier)
0. We end up with machines along random points of the circle.
0. For each key, we similarly hash it as before but using modulo arithmetic, place the resulting hash value on a point on this circle.
0. __The closest machine to this point is responsible for storing this key__.

Now when we add a new machine, it is easy to see how only a couple of keys _(to the left and right of this new machine)_ need to be "re-hashed" and we end up with more "slots" in out DHT.

_I'm obviously glossing over a lot of the intricate details here but hopefully you get the idea_.

## Closing thoughts

You'll find the technique of Consistent Hashing pretty prevalent in DHTs and on
    particular instance of this you might be familiar with is Apache's [Cassandra][].

There are also some caveats to this, as you can imagine.

For instance, the distribution of keys might not be uniform among all machines (due to the way we select points on the circle and the resulting distribution of keys). Cassandra, for instance, chooses manage this by monitoring the load on each machine and moving their locations on the 'circle' accordingly.

Another interesting approach is using 'Virtual Nodes', as described in Amazon's [Dynamo][] paper to overcome this problem.


[Hash Table]: http://en.wikipedia.org/wiki/Hash_table
[amortized]: http://en.wikipedia.org/wiki/Amortized_analysis
[cache]: http://en.wikipedia.org/wiki/Cache_(computing)
[DHT]: http://en.wikipedia.org/wiki/Distributed_hash_table
[modulo]: http://en.wikipedia.org/wiki/Modulo_operation
[Consistent Hashing]: http://en.wikipedia.org/wiki/Consistent_hashing
[Cassandra]: http://cassandra.apache.org/
[Dynamo]: http://www.allthingsdistributed.com/2007/10/amazons_dynamo.html
