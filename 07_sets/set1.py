# Set : It is a data type in python which can hold unique and mixed type of data.
# Features: Unordered, Unique, Mutable, Do not allow indexing

# Creatinf sets
set1 = { 2, 3, "Hello", True, 0, False, 3 + 5j, False}
set2 = set([])

print(set1) # Unorderd and Unique

# Adding element
set1.add(4) 
print(set1)

set1.add((10, 20, 30)) 
print(set1)

set1.update((10, 20, 30))
print(set1)

# Remove elements: remove(), discard(), pop(), clear()
set1.remove(10)
print(set1)

# set1.remove(100)
set1.discard(100)
print(set1)

value = set1.pop()
print(value)

value = set1.pop()
print(value)

set1.clear()
print(set1)


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1 | set2)
print(set1.union(set2))

# Intersection
print(set1 & set2)
print(set1.intersection(set2))


# Subtraction
print(set1 - set2) # 1, 2
print(set2.difference(set1)) # 5, 6

# symmetric_difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

set1 = {1, 2, 3, 4}
set2 = {5}

print(set2.issubset(set1)) # False
print(set1.issuperset(set2)) # False
print(set1.isdisjoint(set2)) # True