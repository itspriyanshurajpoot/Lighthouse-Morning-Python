

# keyword is a module which help us to print the 
# list of keywords


# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword('Falsee'))


# number1 = 635827
# number2 = 36472.55
# name = "ABC"
# isPrime = True
# cn = 4 + 5j
# courses = ['SQL', 'Python', 'Tablue', 'PowerBI']
# classrooms = (1, 2, 3, 4, 5)
# rollNo = {'SI901', 'SI902'}
# details = {
#     "name" : "ABC",
#     "age" : 20,
#     "city" : "Pune"
# }


my_list = [1, "ABC", True, 3 + 5j, True]
my_list[3] = False
print(my_list)

# print(number1, type(number1)) # Output : 635827, type --> int
# print(number2, type(number2)) # Output : 36472.55, type --> float
# print(name, type(name)) # Output : ABC, type --> str
# print(isPrime, type(isPrime)) # Output : True, type --> bool
# print(cn, type(cn)) # Output : 4 + 5j, type --> complex
# print(courses, type(courses)) # Output : ['SQL', 'Python', 'Tablue', 'PowerBI'], type --> list
# print(classrooms, type(classrooms)) # Output : (1, 2, 3, 4, 5), type --> tuple
# print(rollNo, type(rollNo)) # Output : (1, 2, 3, 4, 5), type -> set
# print(details, type(details)) # Output : { "name" : "ABC", "age" : 20,"city" : "Pune"}, type --> dict

# print(cn.real)
# print(cn.imag)

name = 'Rishi Senger'

details = """
    Hello everyone! We are here to learn Python.
    I hope you enjoy the session.
"""

# print(details)

my_set = {34, 34, 56, "ABC", False, True, False}
print(my_set)

# Type casting
x = 10 # int
y = 10.5 # float

z = x + y # float  # Iplicit type casting
print(z, type(z))

name = "ABC"
age = 20

message = "Hello everyone! My name is " + name + " and age is " + str(age) # Developer ---> explicit type casting
print(message)

number = 20
print(number, type(number))

# Convert number from int to str
result = str(number)
print(result, type(result)) # 20 str

# Multiple function
# any type ---> int ---> int()
# any type ---> str ----> str()
# any type ---> float ---> float()
# any type ---> bool ---> bool()
# any type ---> list ---> list()
# any type ---> tuple ---> tuple()
# any type ---> set ---> set()
# any type ---> dictionary ---> dict()

