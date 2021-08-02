"""
Like lists, but they are used for immutable things (that don't change).
Index selalu dari 0
"""

tuples = ('apple','grape','mango','oranges')
print(tuples)
print(tuples[2])
print(tuples[-1])
print(tuples[-2])
print(tuples[3])
print(tuples[::1])
print(tuples[:1])
print(tuples[:-1])
print(tuples[::-2])
print(tuples[0:3:2])
# Immutability
# tuples[1] = 'donuts' # TypeError
# tuples.append('candy')# AttributeError

# Indexing
print(tuples.index('apple'))
print(tuples.count('grape'))


new_tuples = (1,'10','Contoh')
print(new_tuples)