# String: String is a set of characters.

# String declarartion
str1 = "ABC"
str2 = 'MNO'
str3 = """
    This is my multiline string.
    We define using triple diuble quote
"""
str3 = '''
    This is my multiline string.
    We define using triple diuble quote
'''


# Indexing
sentence = "This is a session for python programming."
print(sentence[-4]) # Getting character using index

# Immutable : We can't modify the string object once created.
# sentence[-4] = 'j' # Error

# Slicing : To get a substring from a string
# value = sentence[22:28:1]
# value = sentence[22:28] # step -> 1
# value = sentence[:28:] # start -> 0, step -> 1
# value = sentence[::-1] # Reverse 
value = sentence[:21:-1] # start -> -1
print(value)


# Iterating through string

# Print the vowels present in a string
for ch in sentence:
    if(ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        print(ch)


str1 = "xzchkjAxncnzxkJHAasAjUHA"

for ch in str1:
    ascii = ord(ch)
    if(ascii >= 97 and ascii <= 122):
        print(ch, end=" ")


# Membership operator : in, not in
print("Python" in sentence) # False

# Repitation of string
value = "ABC"
print(value * 3)

# Compare two string : ==
value1 = "ABC"
value2 = "ABC"

a = [1, 2, 3]
b = [1, 2, 3]

print(value1 is value2) # True
print(a is b) # False

# Escape sequence : \n, \t, \'
print("Hello \t everyone")

# It's a rainy season
print("It's a rainy season")

# String formating
name = "Rishi"
age = 22

# My name is Rishi and age is 22

# Comma
print("My name is", name, "and age is", age)

# Concatenation
print("My name is " + name + " and age is " + str(age))

# % formatting
print("My name is %s and age is %d"%(name, age))

# str.format()
print("My name is {} and age is {}".format(name, age))

# f-strings
print(f"My name is {name} and age is {age}")


sentence = "This is a session for python programming."
print(sentence.capitalize())
print(sentence.lower())
print(sentence.upper())
print(sentence.count('i'))
print(sentence.index('i'))
print(len(sentence))