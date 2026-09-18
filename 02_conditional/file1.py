# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# if (a > b) :
#     print(f"{a} is greater")
# else:
#     print(f"{b} is greater")

# num = int(input("Enter a number to check whether it is even or odd "))

# if num % 2 == 0 :
#     print("Even")
# else:
#     print("Odd")


# Marks 
# marks  >= 90 --> Grade A
# marks < 90 and marks >= 80 --> Grade B
# marks < 80 and marks >= 60 --> Grade C
# marks < 60 and marks >= 40 ---> Grade D
# marks < 40 ---> Grade E

marks = float(input("Enter the marks "))

if (marks >= 90) :
    print("Grade A")
else :
    if (marks >= 80):
        print("Grade B")
    else:
        if (marks >= 60):
            print("Grade C")
        else:
            if(marks >= 40):
                print("Grade D") 
            else:
                print("Grade E")

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade E")