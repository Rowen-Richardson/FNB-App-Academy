# CONTROL STATEMENTS = are the fundamental components of programming languages
# that allow us to control the flow of execution based on certain conditions.

# 1. Conditional Statements(if else elif)
# num = 10
# if num > 0: 
#     print("Positive number")

num = 0
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number or zero")

num1 =int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print("Both numbers are equal.")