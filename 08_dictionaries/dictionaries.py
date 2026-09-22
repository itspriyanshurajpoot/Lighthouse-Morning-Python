# Dictionary: Stores data in a key value pair
# Ordered
# Mutable
# Key should be unique

# Creating a dictionaries
dict1 = dict({
    "name" : "ABC",
    "age" : 20,
    "rollNo" : 21,
    "city" : "Pune"
})

print(dict1)

print("------------------------")
# Accessing values
print(dict1['city'])

print("-------------------------")

# In-built functions
print(dict1.keys()) # List of keys
print(dict1.values()) # List of values
print(dict1.items()) # List of key value pairs tuples

print("-------------------------")

# Iterating through dictionaries
for element in dict1: # Getting keys and values without using in-build functions
    print(element, dict1[element])

print("-------------------------")

for element in dict1.values(): # Getting list of values
    print(element)

print("-------------------------")

for element in dict1.keys(): # Getting list of keys
    print(element)

print("-------------------------")

for key, value in dict1.items():
    print(key, value, sep=":")

student = {
    "name" : "Rajan",
    "age" : 21,
    "course" : ["Python", "SQL", "PowerBI", "Excel"],
    "address" : {
        "city" : "Pune",
        "pincode" : 232321,
        "state" : "Maharashtra"
    }

}

print(student["address"]["pincode"])

# Adding new element
student["fees"] = 3000000
student['address']['district'] = 'Pune' 

print(student)

# # Updating the existing element
# student["age"] = 25
# print(student)

# value = student.pop('fees')
# print(student, value)

# value = dict1.popitem()
# print(value)


# Homework : Create an application in which store the list of details of multiple students where a new student can be added, existing student can update their value or delete their record or search their record.
