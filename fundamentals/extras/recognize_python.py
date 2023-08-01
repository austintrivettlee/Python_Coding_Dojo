num1 = 42  # Variable Declaration
num2 = 2.3  # Variable Declaration
boolean = True  # Variable Declaration
string = "Hello World"  # Variable Declaration
pizza_toppings = [
    "Pepperoni",
    "Sausage",
    "Jalepenos",
    "Cheese",
    "Olives",
]  # Variable Declaration
person = {
    "name": "John",
    "location": "Salt Lake",
    "age": 37,
    "is_balding": False,
}  # Variable Declaration
fruit = ("blueberry", "strawberry", "banana")  # tuple Declaration
print(type(fruit))  # Type Check
print(pizza_toppings[1])  # Log Statement
pizza_toppings.append("Mushrooms")  # List - Add Value
print(person["name"])  # Dictionary - Access value
person["name"] = "George"  # Dictionary change value
person["eye_color"] = "blue"  # Dictionary Add Value
print(fruit[2])  # Access Tuple Value

if num1 > 45:  # Conditional if
    print("It's greater")  # Log Statement
else:  # Conditional Else
    print("It's lower")  # Log Statement

if len(string) < 5:  # Conditional if
    print("It's a short word!")  # Log Statement
elif len(string) > 15:  # Conditional elif
    print("It's a long word!")  # Log Statement
else:  # Conditional Else
    print("Just right!")  # Log Statement

for x in range(5):  # for loop start increment
    print(x)  # Log Statement
for x in range(2, 5):  # for loop start increment
    print(x)  # Log Statement
for x in range(2, 10, 3):  # for loop start increment
    print(x)  # Log Statement
x = 0  # Variable Declaration
while x < 5:  # while loop start
    print(x)  # Log Statement
    x += 1  # while loop increment

pizza_toppings.pop()  # list delete value
pizza_toppings.pop(1)  # list delete value

print(person)  # Log Statement
person.pop("eye_color")  # Dictionary delete value
print(person)  # Log Statement

for topping in pizza_toppings:  # For loop increment
    if topping == "Pepperoni":  # conditional if statement
        continue  # for loop continue
    print("After 1st if statement")  # Log Statement
    if topping == "Olives":  # if statement
        break  # for loop end


def print_hello_ten_times():  # function argument
    for num in range(10):  # for loop
        print("Hello")  # log statement


print_hello_ten_times()  # function call and return


def print_hello_x_times(x):  # Function argument
    for num in range(x):  # for loop increment
        print("Hello")  # log statement


print_hello_x_times(4)  # function call and return


def print_hello_x_or_ten_times(x=10):  # Function argument
    for num in range(x):  # for loop
        print("Hello")  # log statement


print_hello_x_or_ten_times() # function call and return
print_hello_x_or_ten_times(4) # function call and return with an argument


"""
Bonus section
"""

print(num3) # NameError: name <variable name> is not defined
num3 = 72
fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) #KeyError: 'favorite_team'
print(pizza_toppings[7]) # IndexError: list index out of range
print(boolean) #IndentationError: unexpected indent
fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'
