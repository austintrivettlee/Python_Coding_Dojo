"""
Python Functions
"""


def greet(name: str):
    print("Hello, " + name)

greet("Kenneth")

def greet_with_return(name):
    return "Hello, " + name

greeting = greet_with_return("Elle")

print(greeting)

"""
Scope in functions
Scope is the block of code where a variable exists
"""

def multiply(a, b):
    result = a * b
    return result

x = 3
y = 4
product = multiply(x, y)
print(product)