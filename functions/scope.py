global_var = "I am global variable"

def outer_function():
    global global_var
    global_var = "I am local variable of outer function"
    local_var = "I am local to outer function"

    def inner_function():
        # print(local_var) # 1. I am local to outer function
        pass

    inner_function()
    # print(local_var) # 2: I am local to outer function
    # print(global_var) # 3: I am local variable of outer function


outer_function()
# print(global_var) # I am local variable of outer function

# Return 
# def sum(a, b):
#     sum = a + b
#     return  sum


# value = sum(2, 3)
# print(value)

def outer_function():
    print("I am local to outer function")

    def inner_function():
        print("I am inner function")

    return inner_function

inner = outer_function()
inner()


def base(b):
    def pwr(p):
        print(b ** p)

    return pwr

pwr1 = base(6)
pwr1(2)

pwr2 = base(3)
pwr2(2)

# Lambda
# def sum(a, b):
#     return a + b

sum = lambda a, b: a + b;

value = sum(2, 3)
print(value)

