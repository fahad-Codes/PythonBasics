# Exception Handling in Python

# Exception handling allows you to gracefully handle errors and exceptions that may occur during program execution.

# Example 1: Handling a Specific Exception

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Explanation:
# - I've used a 'try' block to enclose the code that might raise an exception.
# - I've used an 'except' block to handle a specific exception (ZeroDivisionError).
# - The 'as e' clause allows us to capture the exception object for further analysis.

# Example 2: Handling Multiple Exceptions

try:
    result = int("abc")
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Explanation:
# - I've used multiple 'except' blocks to handle different types of exceptions.

# Example 3: Handling Any Exception

try:
    result = 10 / 0
except Exception as e:
    print(f"Error: {e}")

# Explanation:
# - Using 'Exception' as the base class of exceptions allows you to catch any type of exception.

# Example 4: Handling Unspecified Exception

try:
    result = 10 / 0
except:
    print("An error occurred")

# Explanation:
# - Catching exceptions without specifying a specific type can be done, but it's generally recommended to specify the type.

# Example 5: Handling Multiple Exceptions in One Except Block (Tuple of Exceptions)

try:
    result = int("abc")
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

# Explanation:
# - You can handle multiple exceptions in one 'except' block by providing a tuple of exception types.

# Example 6: Handling Exceptions with Finally

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Execution completed")

# Explanation:
# - The 'finally' block is executed regardless of whether an exception occurred or not. It is commonly used for cleanup operations.

# Raising Custom Exceptions:

# Example 7: Raising a Custom Exception


class CustomError(Exception):
    pass


try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Error: {e}")

# Explanation:
# - You can create custom exceptions by inheriting from the 'Exception' class.

# Related Functions:

# - raise: Used to raise an exception.
# - assert: Used to test if a condition is true, and raises an exception if not.

# Exception handling is a crucial aspect of writing robust and reliable Python code.
