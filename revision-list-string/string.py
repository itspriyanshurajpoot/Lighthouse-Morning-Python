str1 = "ABC"
str2 = 'ABC'
str3 = """
    This is a multi line string.
    We define using double quote
"""
str4 = '''
    This is also a multi line string
    using single triple quote.
'''

# print(str1, type(str1))
# print(str2, type(str2))
# print(str3, type(str3))
# print(str4, type(str4))

# Indexing

value = "SEED Infotech"
# print(value[-10])
# print(value[6])

# Slicing
substr = value[5:12:1] # Infotec
substr = value[12:4:-1] # hcetofnI
substr = value[5:13:2] # Iftc
substr = value[:13:] # SEED Infotech
substr = value[::] # SEED Infotech
substr = value[::-1] # # hcetofnI DEES
# print(substr)

name = "Arpit"

# Iterating over string
# for char in name:
#     print(char)



# Print the vowels present in a string
for char in value:
    # if (char == 'A' or char == 'I' or char == 'E' or char == 'O' or char == 'U' or char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
    #     print(char, end=" ")
    vowels = "AEIOUaeiou"
    if (char in vowels):
        print(char)


# Print all capital letters present in a string
value = "AKJHDsuaysaNJHAKSSAshdoaAHH-"
for char in value:
    ascii = ord(char) # 65
    # if (ascii >= 65 and ascii <= 90): # Capial letter
    #     print(char, end=" ")
    if(ascii >= 97 and ascii <= 122):
        print(chr(ascii), end=" ")


# Compare two string
str1 = "ABC"
str2 = "ABC"

print(str1 == str2)

# String is immuable
print(str1[2])
# str1[2] = "D"

print("Hello's world")

value = "AKJHDsuaysaNJHAKSSAshdoaAHH-"
print(value.capitalize())
print(value.upper())
print(value.lower())
print(value.find('x'))
print(value.index('x'))
print(len(value))