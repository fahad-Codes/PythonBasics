# Functions, Built-in Functions, and Variable Scope in Python

# Functions:
# Functions are blocks of reusable code that perform a specific task. They allow for code modularity and reusability.

# Example 1: Simple Function

# Define a function named 'greet'
def greet(name):
    """This function greets the user."""
    print(f"Hello, {name}!")


# Call the function
greet("Alice")

# Explanation:
# - In this example, a function named 'greet' is defined using the 'def' keyword.
# - It takes one parameter 'name'.
# - The function body contains a print statement that greets the user with the provided name.
# - The function is then called with the argument "Alice", resulting in "Hello, Alice!" being printed.

# Example 2: Function with Return Value

# Define a function named 'add'


def add(a, b):
    """This function adds two numbers and returns the result."""
    result = a + b
    return result


# Call the function
sum_result = add(3, 5)
print(f"The sum is: {sum_result}")

# Explanation:
# - In this example, a function named 'add' is defined. It takes two parameters, 'a' and 'b'.
# - Inside the function, 'a' and 'b' are added, and the result is stored in the variable 'result'.
# - The 'return' statement is used to send the result back to the caller.
# - The function is called with arguments 3 and 5, and the returned value (8) is printed.

# Built-in Functions:

# Python provides a wide range of built-in functions that can be used without the need for additional imports.

# Example 3: Built-in Functions

# len(): Returns the length of a sequence (e.g., string, list).
length = len("Hello")  # Result: 5

# print(): Outputs the specified message to the console.
print("Hello, World!")

# int(): Converts a value to an integer.
int_value = int("42")  # Result: 42

# str(): Converts a value to a string.
str_value = str(42)  # Result: "42"

# range(): Generates a sequence of numbers.
range_sequence = range(5)  # Result: [0, 1, 2, 3, 4]

# Example 4: More Useful Built-in Functions

# abs(): Returns the absolute value of a number.
abs_value = abs(-10)  # Result: 10

# max(): Returns the largest item in an iterable or the largest of two or more arguments.
max_value = max(5, 2, 8, 1, 6)  # Result: 8

# min(): Returns the smallest item in an iterable or the smallest of two or more arguments.
min_value = min(5, 2, 8, 1, 6)  # Result: 1

# sum(): Returns the sum of all items in an iterable.
sum_result = sum([1, 2, 3, 4, 5])  # Result: 15

# all(): Returns True if all elements of the iterable are true.
all_true = all([True, True, True])  # Result: True

# any(): Returns True if at least one element of the iterable is true.
any_true = any([False, False, True])  # Result: True

# sorted(): Returns a sorted list from the specified iterable.
# Result: [1, 1, 2, 3, 4, 5, 6, 9]
sorted_list = sorted([3, 1, 4, 1, 5, 9, 2, 6])

# reversed(): Returns a reversed iterator of a sequence.
reversed_list = list(reversed([1, 2, 3, 4]))  # Result: [4, 3, 2, 1]

# Variable Scope:

# The scope of a variable defines where in the code a variable is accessible.

# Example 5: Variable Scope

x = 10  # Global variable


def my_function():
    """This function demonstrates variable scope."""
    y = 20  # Local variable
    print(f"x inside function: {x}")  # Access global variable
    print(f"y inside function: {y}")  # Access local variable


# Call the function
my_function()

# print(f"x outside function: {x}")  # This would raise an error because 'y' is not defined outside the function

# Explanation:
# - In this example, 'x' is a global variable, meaning it can be accessed anywhere in the code.
# - 'y' is a local variable, meaning it is only accessible within the function 'my_function'.
# - The function accesses both 'x' and 'y' and prints their values.
# - Trying to access 'y' outside the function would result in an error.

# Functions, built-in functions, and variable scope are important concepts in Python for organizing code and managing data.
