my_list = [45, 45, 32, "Hello", True, 45.5] # Hetegeneous list
my_list = [45, 65, 54, 32, 45] # Homogeneous list

print(my_list) # Ordered, Duplicate
my_list[-2] = 34 # Mutable
print(my_list)

# Indexing
print(my_list[-2]) # 34
print(my_list[2]) # 54

my_list = [45, 65, [34, 54, 'Hello', [30, 20, 50, True], True], 32, 45]
print(my_list[2][2]) # Hello
print(my_list[3])
print(my_list[2][3][3])

# Slicing
print(my_list[2][3][1::])
print(my_list[2][2:-1:])


# Iterating
marks = [78, 87, 88, 67, 80]
# for item in marks:
#     print(item + 1, end=" ")

# Add elements : append(), extend(), insert()
marks.append(90)
print(marks)

marks.extend([89, 92, 93])
print(marks)

marks.append([89, 92, 93])
print(marks)

marks.insert(1, 89)
print(marks)

# Modifing elements
marks[0] = 30
print(marks)

marks[0:2:1] = 40, 88
print(marks)

# Delete elements
marks.remove(88)
print(marks)

element = marks.pop(-3)
print(element, marks)

del marks
print(marks)

# marks.clear()
# print(marks)