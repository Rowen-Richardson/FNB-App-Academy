# FUNCTIONS are a fundamental way to structure a code in python
# They allow you to encapturade a piece of code and reuse it again in your code
# They can contain loops, conditional statements and other functions
'''
def greet(name):
    print(f"Hello, {name}") 

greet("Alice") 

def add(a, b):
    return a + b
result = add(2, 5)
print(result)
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Steve", "Good Morning")