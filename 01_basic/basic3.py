# Arithmatic Operator : + , -, *, /, //, %, **
a = 10
b = 4
print(a + b) # 14
print(a - b) # 6
print(a * b) # 40
print(a / b) # 2.5
print(a // b) # 2
print( a % b) # 2
print(a ** b) # 10000

# Assignment Operator : =, +=, -=,, *=, /=, //=, %=, **=
x = 20
y = 30

x += y
print(x)

# Comparison operator : <, <=, >, >=, ==, !=
m = 10
n = 10

print(m > n) # False
print(m >= n) # True
print(m < n) # False
print(m <= n) # True
print(m == n) # True
print(m != n) # False

print("----------------------------------------")
# Identity operator : is , is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True
print(a is not b) # False
print(a is c) # False
print(a == c) # True

print("=----------------------------------------")

# Membership operator : in, not in
a = [True, "Hello", 23, 43.5, "ABC"]
b = "hello"

print(b in a) # False
print(b not in a) # True