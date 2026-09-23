
# Declare function
def my_sum(a, b):
    print(f"Sum is {a + b}")

# Call the function
my_sum(2, 3)


# Types of functions based on function argunments
# Positional argunments
def differenceOfTwoNumber(a, b):
    print(f"Difference is {a - b}")

differenceOfTwoNumber(2, 3) # -1
differenceOfTwoNumber(3, 2) # 1

# Default argunments
def simpleInterest(principal, time, rate=3.4):
    print(f"Simple intrest is {principal * rate * time / 100}")

simpleInterest(30000, 2)

# Named argunment
differenceOfTwoNumber(b = 3, a = 2) # -1

# Variable length argunment : *args
def sumOfElements(*elements):
    sum = 0
    for element in elements:
        sum = sum + element

    print("Sum of elements is", sum)

sumOfElements(3, 5, 6, 7)

# Arbitrary key worded argunments
def keyWordedArgunements(**elements) :
    for key, element in elements.items():
        print(key, element, sep=":")


keyWordedArgunements(name="ABC", age = 21)

# list1 = [[1, 2, 3], 
#          [4, 5, 6], 
#          [7, 8, 9]]

# for element in list1:
#     for value in element:
#         print(value)    

def outer_function():
    print("I am outer function")

    def inner_function():
        print("I am inner function")

    inner_function()


outer_function()

