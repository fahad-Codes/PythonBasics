# Lambda Expressions and Predicates in Python

# Lambda Expressions:

# Lambda expressions (lambda functions) are anonymous functions that can be defined without a name.
# They are useful for creating small, one-off functions.

# Example 1: Creating a Lambda Function

def square(x): return x**2


result = square(5)  # Result: 25

# Explanation:
# - I've created a lambda function 'square' that takes one argument 'x' and returns 'x**2'.
# - This lambda function can be used like a regular function.

# Example 2: Using Lambda with map()

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

# Result: [1, 4, 9, 16, 25]

# Explanation:
# - I've used a lambda function with the 'map()' function to apply the function to each element in the 'numbers' list.

# Predicates:

# Predicates are functions that return a boolean value (True or False).
# They are commonly used for filtering data based on a condition.

# Example 3: Creating a Predicate


def is_even(x): return x % 2 == 0


result_1 = is_even(4)  # Result: True
result_2 = is_even(3)  # Result: False

# Explanation:
# - I've created a predicate 'is_even' that checks if a number is even.
# - It returns True if the number is divisible by 2, otherwise, it returns False.

# Example 4: Using Predicate with filter()

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Result: [2, 4]

# Explanation:
# - I've used a lambda function as a predicate with the 'filter()' function to filter even numbers from the 'numbers' list.

# Related Functions:

# - map(): Applies a function to all items in an input list and returns an iterator with the results.
# - filter(): Filters elements from an iterable for which a function returns true.

# Lambda expressions and predicates are powerful tools in Python for creating concise and functional-style code.
