# Tuple :
# Sequence Data Type
# Ordered
# Can contain homogeneous and heterogeneous elements
# Allow dublicate
# Immutable


# Create Tuple
tuple1 = (1, 2, 3, "Hello", True, 34.5)
tuple2 = tuple([1, 2, 3, "Hello", "World"])

print(tuple1, type(tuple1))
print(tuple2, type(tuple2))

# Accessing elements

# Indexing
print(tuple1[-2]) # True

# Slicing
tuple3 = (1, 2, 3, "Hello", [34, 54, 'Hello', (30, 20, 50, True), True], 32, 45)
print(tuple3[4][3][0]) # Indexing

print(tuple3[4][2:-1:1]) # Slicing

# Immutable
# tuple1[-2] = False

list1 = [1, 2, 3, 4, 5]

# Iterate
for index, element in enumerate(tuple3):
    print(index, element)


# Concatination
new_tuple = tuple1 + tuple2
print(new_tuple)

# Repitation
new_tuple = tuple1 * 2
print(new_tuple)

# Packing : When we try to store multiple value in a single variable
a = 2, 3, "Hello", False
print(a, type(a))

# Unpacking : When we try to store the value of a single tuple into multiple variable
a, b, c, d = a
print(a, b, c, d)

# Tuple methods : count(), index()
my_tuple = (1, 2, 3, 1, 4, 1, 4)
print(my_tuple.count(1))
print(my_tuple.index(1))
