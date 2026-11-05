# Sets are unordered, unindexed, and mutable, unchangeable items
# Sets don't support duplicates values

s= {1, 2, 3, 3, 4, 5}
#print(s, s[1])# we can't perform indexing on sets
#s[2] = 300 # sets are immutable , so we cannot add  or remove elements
s.add(7)
s.update({8, 9})
#s.remove(10)
s.discard(10)
#s.pop()
s.pop()
#s.clear()
#del s
print(s, type(s))

s1 = {1, 2, 3, "hello",1.2, True, (10,20), None}
print(s1)

#constructor
s2 = set()
print(s2, type(s2))# empty set
s3 = set([1, 2, 3, 4])
print(s3, type(s3))

## how to access random number without INDEXING
fs = frozenset([1,2,3])
print(fs,type(fs))
#fs.add(6) ## we can't add because it will create new frozenset object and it is immutable
