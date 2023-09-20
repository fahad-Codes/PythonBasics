# Enums and Constants in Python

# Enums:
# Enums are a way to represent a group of symbolic names (constants) bound to unique values.
# They provide a way to define a set of related named constants.

# Constants:
# Constants are variables whose values do not change during program execution.
# In Python, there is no strict concept of constants, but developers often use uppercase names
# to denote variables that are intended to be treated as constants.

# Enums Example:

from enum import Enum, auto

# Define an Enum class


class Colors(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

# Enums provide a way to represent a fixed set of choices.
# In this example, Colors.RED, Colors.GREEN, and Colors.BLUE are symbolic names for unique values.

# Constants Example:


# Define constants (usually using uppercase names)
PI = 3.14
MAX_CONNECTIONS = 100

# Constants are typically used for values that should not be changed during program execution.
# In this example, PI and MAX_CONNECTIONS are treated as constants.

# Example Usage:


def calculate_area(radius):
    area = PI * (radius ** 2)
    return area


# Using Enums
color = Colors.RED
if color == Colors.RED:
    print("The color is red")

# Using Constants
radius = 5
area = calculate_area(radius)
print(f"The area of a circle with radius {radius} is {area}")

'''
Enums:

I've imported the Enum class from the enum module.
Created an Colors enum class with members RED, GREEN, and BLUE using the auto() function.
Enums provide a way to represent a fixed set of choices. In this example, we can use Colors.RED, Colors.GREEN, and Colors.BLUE to represent these choices.

Constants:

Defined constants PI and MAX_CONNECTIONS with values 3.14 and 100 respectively. These are conventionally written in uppercase to indicate that they are intended to be treated as constants.
Constants are typically used for values that should not be changed during program execution.
Example Usage:

I've defined a function calculate_area(radius) that calculates the area of a circle using the constant PI.
I've demonstrated using Enums by assigning Colors.RED to the variable color and checking if it's red.
Lastly, I've calculated the area of a circle using the constant PI.
'''
