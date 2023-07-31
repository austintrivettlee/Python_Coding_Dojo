import math

# popular programming language
# created by Guido van Rossum - Released 1991
# it is an interpreted language - not a compiled
# named after monty python

# used for web development, A.I., automation and scripting, data science and scientific computing
# Why Python?
# Readability and simplicity
# Easy to learn and versatile

# String Creation
print("this is a string".title())
my_string = "this is a string"
print(my_string.center(50, "*"))

# Constructor function
my_other_string = str("Another String")
print(my_other_string)
my_number = 56
print(type(my_number))
stringified = str(my_number)
print(type(stringified))

# Print function
print("Hello World")

# Type Function
type(my_string)

# Concatenation
hello = "Hello "
world = "World"

hello_world = hello + world
print(hello_world)
# print(hello_world + 5) # Error
print(hello_world + str(5))

# String Method
print(hello_world.rsplit(" "))  # Splits a string based on a separator

# Upper, Lower, Title
print(hello_world.upper())
print(hello_world.lower())
print(hello_world.title())

#  Length
print(len(hello_world))
print(len("sup bro"))

# strip
whitespace_string = "    hello    "
stripped = whitespace_string.strip()
print(stripped)

# boolean
is_awake = True


# Arithmetic operators
# +, -, /, *, **, //
# int
num_of_scoops = 2
# float
pi = 3.14159
print(2**3)
print(6 // 2)
print(6 / 2)

# +=, -=, *=, /= assignment combinators

x = 2
x = x + 8
x += 8  # alternate to above

# sqrt ceil floor
print(math.ceil(pi))
print(math.floor(pi))
print(math.sqrt(pi))

# why use none?
# sometimes we want values to be optional
# to control code flow

# constructor functions and casting
five = "5"
print(type(five))
int_five = int(5)
print(type(int_five))

string_true = "True"
bool_true = bool(string_true)
print(type(bool_true))
print(bool_true)

# List Creation

colors = ["purple", "cornflour yellow", "golden rod", "firebrick", "dark orchid"]