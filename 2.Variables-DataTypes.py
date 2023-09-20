# Variables in Python

# A variable is a named location in memory used to store data.
# It allows us to manipulate and work with data in our programs.

# Variable Naming Rules:
# 1. Variable names can only contain letters, digits, and underscores (_).
# 2. Variable names cannot start with a digit.
# 3. Variable names are case-sensitive (e.g., 'myVar' and 'MyVar' are different).

# Example:

# Assigning values to variables
my_integer = 10  # Integer variable
my_float = 3.14  # Floating-point variable
my_string = "Hello, World!"  # String variable
my_boolean = True  # Boolean variable

# Printing variables
print(my_integer)  # Output: 10
print(my_float)    # Output: 3.14
print(my_string)   # Output: Hello, World!
print(my_boolean)  # Output: True

# Data Types in Python

# Data types define the type of value that a variable can hold.
# Python has various built-in data types, including integers, floats, strings, and booleans.

# Integer
# - Whole numbers without decimal points.
# - Example: 10, -5, 0

# Float (Floating-Point)
# - Numbers with decimal points or in exponential form.
# - Example: 3.14, -0.5, 2.0e3 (2.0 multiplied by 10 to the power of 3)

# String
# - A sequence of characters enclosed in single, double, or triple quotes.
# - Example: "Hello", 'Python', '''Multi-line string'''

# Boolean
# - Represents truth values: True or False.
# - Used for conditions and logical operations.

# Example:

# Integer
my_integer = 10

# Float
my_float = 3.14

# String
my_string = "Hello, Python!"

# Boolean
my_boolean = True

# Checking data types using the type() function
print(type(my_integer))  # Output: <class 'int'>
print(type(my_float))    # Output: <class 'float'>
print(type(my_string))   # Output: <class 'str'>
print(type(my_boolean))  # Output: <class 'bool'>
