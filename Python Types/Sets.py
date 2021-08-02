"""
Unordered collection of unique elements.
No Duplicate Value
"""

list = [1,2,3,4,5,6]
print(set(list))

print('----')
set = {4,5,6}
print(set)
set.add(1)
print(set)
set.add(1)
set.add(10)
print(set)

# Basic Functions
set.remove(10)
print(set)
set.discard(10)
print(set)
set.clear()
print(set)
newSet = set.copy()
print(newSet)

# Set Functions
print('----')
set1 = {1,2,3,4}
set2 = {4,5,6}
print(set1.union(set2)) # Gabungan
print(set1.intersection(set2)) # irisan
print(set1.difference(set2)) # set1 - set2
print(set1.symmetric_difference(set2)) # set1(complement) ∪ set2(complement)
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))

set_new = {1,2,'12'}
print(set_new)
set_new.remove('12')
print(set_new)