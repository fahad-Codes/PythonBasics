# Operators and Related Functions in Python

# Operators are special symbols that perform operations on operands (variables and values).
# Python supports various types of operators, including arithmetic, comparison, logical, assignment, etc.

# Arithmetic Operators:

# Addition (+): Adds two operands.
addition_result = 10 + 5  # Result: 15

# Subtraction (-): Subtracts the right operand from the left operand.
subtraction_result = 10 - 5  # Result: 5

# Multiplication (*): Multiplies two operands.
multiplication_result = 10 * 5  # Result: 50

# Division (/): Divides the left operand by the right operand.
division_result = 10 / 5  # Result: 2.0 (Note: Always returns a float)

# Modulus (%): Returns the remainder of the division.
modulus_result = 10 % 3  # Result: 1

# Exponentiation (**): Raises the left operand to the power of the right operand.
exponentiation_result = 2 ** 3  # Result: 8

# Floor Division (//): Returns the floor of the division.
# Result: 3 (Rounds down to the nearest integer)
floor_division_result = 10 // 3

# Comparison Operators:

# Equal to (==): Checks if two operands are equal.
is_equal = (10 == 5)  # Result: False

# Not equal to (!=): Checks if two operands are not equal.
not_equal = (10 != 5)  # Result: True

# Greater than (>): Checks if the left operand is greater than the right operand.
greater_than = (10 > 5)  # Result: True

# Less than (<): Checks if the left operand is less than the right operand.
less_than = (10 < 5)  # Result: False

# Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.
greater_than_or_equal = (10 >= 5)  # Result: True

# Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.
less_than_or_equal = (10 <= 5)  # Result: False

# Logical Operators:

# and: Returns True if both operands are true.
logical_and = True and False  # Result: False

# or: Returns True if at least one operand is true.
logical_or = True or False  # Result: True

# not: Returns True if the operand is false, and vice versa.
logical_not = not True  # Result: False

# Assignment Operators:

# =: Assigns the value of the right operand to the left operand.
x = 10  # x is now 10

# +=: Adds the right operand to the left operand and assigns the result to the left operand.
x += 5  # Equivalent to: x = x + 5 (x is now 15)

# -=: Subtracts the right operand from the left operand and assigns the result to the left operand.
x -= 3  # Equivalent to: x = x - 3 (x is now 12)

# *=: Multiplies the left operand by the right operand and assigns the result to the left operand.
x *= 2  # Equivalent to: x = x * 2 (x is now 24)

# /=: Divides the left operand by the right operand and assigns the result to the left operand.
x /= 4  # Equivalent to: x = x / 4 (x is now 6.0)

# %=: Calculates the modulus of the left operand with the right operand and assigns the result to the left operand.
x %= 5  # Equivalent to: x = x % 5 (x is now 1.0)

# **=: Raises the left operand to the power of the right operand and assigns the result to the left operand.
x **= 2  # Equivalent to: x = x ** 2 (x is now 1.0)

# //=: Performs floor division and assigns the result to the left operand.
x //= 0.5  # Equivalent to: x = x // 0.5 (x is now 2.0)

# Bitwise Operators:

# Bitwise AND (&): Performs a bitwise AND operation.
bitwise_and = 5 & 3  # Result: 1 (Binary: 0101 & 0011 = 0001)

# Bitwise OR (|): Performs a bitwise OR operation.
bitwise_or = 5 | 3  # Result: 7 (Binary: 0101 | 0011 = 0111)

# Bitwise XOR (^): Performs a bitwise XOR (exclusive OR) operation.
bitwise_xor = 5 ^ 3  # Result: 6 (Binary: 0101 ^ 0011 = 0110)

# Bitwise NOT (~): Performs a bitwise NOT (complement) operation.
# Result: -6 (Binary: ~0101 = 1010, in two's complement form, this represents -6)
bitwise_not = ~5

# Left Shift (<<): Shifts the bits of the left operand to the left by a specified number of positions.
left_shift = 5 << 1  # Result: 10 (Binary: 0101 << 1 = 1010)

# Right Shift (>>): Shifts the bits of the left operand to the right by a specified number of positions.
right_shift = 5 >> 1  # Result: 2 (Binary: 0101 >> 1 = 0010)

# Membership Operators:

# in: Returns True if the specified element exists in the specified sequence.
in_operator = 3 in [1, 2, 3]  # Result: True

# not in: Returns True if the specified element does not exist in the specified sequence.
not_in_operator = 4 not in [1, 2, 3]  # Result: True

# Identity Operators:

# is: Returns True if both variables are the same object.
x = [1, 2, 3]
y = [1, 2, 3]
is_operator = x is y  # Result: False (x and y are distinct objects)

# is not: Returns True if both variables are not the same object.
is_not_operator = x is not y  # Result: True

# Ternary Conditional Operator:

# The ternary conditional operator allows for conditional expressions in a concise form.
# It has the form: expression_if_true if condition else expression_if_false

result = "Greater" if 10 > 5 else "Lesser"  # Result: "Greater"

# Operator Precedence:

# Operator precedence determines the order in which operations are performed.
# Parentheses can be used to control the order of operations.

# Result: 20 (Multiplication has higher precedence)
precedence_example = 10 + 5 * 2

# Functions for Mathematical Operations:

# abs(): Returns the absolute value of a number.
abs_value = abs(-10)  # Result: 10

# round(): Rounds a number to the nearest integer.
rounded_value = round(3.7)  # Result: 4

# pow(): Raises a number to a specified power.
power_result = pow(2, 3)  # Result: 8 (2^3)

# divmod(): Returns the quotient and remainder of division.
quotient, remainder = divmod(10, 3)  # Quotient: 3, Remainder: 1

# sum(): Returns the sum of all items in an iterable.
sum_result = sum([1, 2, 3, 4, 5])  # Result: 15

# min(): Returns the smallest item in an iterable.
min_value = min([5, 2, 8, 1, 6])  # Result: 1

# max(): Returns the largest item in an iterable.
max_value = max([5, 2, 8, 1, 6])  # Result: 8

# All the operators and related functions provide powerful tools for performing various operations in Python.
