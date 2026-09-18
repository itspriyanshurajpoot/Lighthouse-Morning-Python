# Creating list
my_list1 = [23, 45, -45, 32, 21] # Homogenoeour
my_list2 = [23, True, "Hello", 3 + 5j] # Heterogeneous

print(my_list2) # Ordered

my_list3 = list((23, 32, 43, "Python"))
print(my_list3, type(my_list3))


# Indexing and slicing
list1 = [1, 2, 3, 4, [3, 4, 5, "Python", [5, 5, 3], 7, 8, 9], 10, 22, 11]

print(list1[4][4][1]) # Indexing
print(list1[4][5]) # Indexing
print(list1[4][3:7:1]) # Slicing


# Iterating on a list
list2 = [1, 2, 3, 4, 5]

for element in list2 :
    print(element, end=" ")

print("------------------------------")


# Print the target element present in a list
marks = [87, 88, 76, 60, 62]
# target = 61
# for index, element in enumerate(marks) :
#     if(element == target):
#         print(index)
#         break
# else:
#     print("Not present")  


# Adding elements in a list: append(), entend(), insert()
print(marks)
marks.append(87)
print(marks)

marks.extend([76, 80, 90])
print(marks)

# marks.append([100, 99, 98])
# print(marks)

marks.insert(1, 100)
print(marks)

# Modify
marks[1] = "Python"
print(marks)

# Delete element from list: remove(), pop(), clear()
# marks.remove(776) # If the element is not present in the list, it will raise and error : ValueError
print(marks)

element = marks.pop(-2)
print(element, marks)

# marks.clear()
# print(marks)


del marks[-3]
print(marks)

del marks
print(marks)