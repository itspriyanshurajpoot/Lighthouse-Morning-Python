# Question : Take an input from the user and print the input and it's data type

# input() : It helps to take input from the user.
# print() : It helps to display the output in the terminal


# value = input("Enter your input : ") # 25 --> input() always accept value as str.
# print(value, type(value)) # 25, data type --> str\


# Question : I want to take two numbers from the user, add it and display it

# Take two input
# num1 = float(input("Enter the first number : ")) # "23.3"
# num2 = int(input("Enter the second number : ")) # "20"

# sum1 = num1 + num2
# print(sum1) # 43

name = "Rishi"
age = 21

# My name is Rishi and age is 21
print("My name is", name, "and age is", age, end="\n", sep=" ") # First method : Using ,
print("My name is " + name + " and age is " + str(age)) # Second method : Using + (concatenation)
print("My name is %s and age is %d"%(name, age)) # Third way : Using % 
print("My name is {} and age is {}".format(name, age)) # Fourth way : Using str.format()
print(f"My name is {name} and age is {age}")
