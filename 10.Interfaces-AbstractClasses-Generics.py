# Interfaces / Abstract Classes and Generics in Python

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# Abstract Classes (Interfaces):

# An abstract class is a class that contains one or more abstract methods.
# Abstract methods are declared but they don't contain any implementation.
# Subclasses of an abstract class must provide implementations for all abstract methods.


class Shape(ABC):  # Shape is an abstract class (interface)
    @abstractmethod
    def area(self) -> float:
        """
        Abstract method for calculating the area.
        Subclasses must implement this method.
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Abstract method for calculating the perimeter.
        Subclasses must implement this method.
        """
        pass


class Circle(Shape):  # Circle implements Shape interface
    def __init__(self, radius: float):
        """
        Initialize a Circle with a given radius.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Calculate the area of the Circle.
        """
        return 3.14 * self.radius**2

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the Circle.
        """
        return 2 * 3.14 * self.radius


class Square(Shape):  # Square implements Shape interface
    def __init__(self, side_length: float):
        """
        Initialize a Square with a given side length.
        """
        self.side_length = side_length

    def area(self) -> float:
        """
        Calculate the area of the Square.
        """
        return self.side_length**2

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the Square.
        """
        return 4 * self.side_length

# Using Abstract Classes:


circle = Circle(5)
square = Square(4)

circle_area = circle.area()  # Result: 78.5
circle_perimeter = circle.perimeter()  # Result: 31.4

square_area = square.area()  # Result: 16
square_perimeter = square.perimeter()  # Result: 16


# Generics using Type Hints:

# In Python, generics are not enforced at runtime, but they provide useful information for static type checkers.

# Generics allow us to create classes, functions, and data structures that can work with any data type.
# They provide flexibility and type safety in our code.

T = TypeVar('T')  # Declare a type variable T


class Box(Generic[T]):  # Box is a generic class
    def __init__(self, item: T):
        """
        Initialize a Box with an item of type T.
        """
        self.item = item

    def get_item(self) -> T:
        """
        Get the item stored in the Box.
        """
        return self.item

# Using Generics:

# ...

# Explanation:

# Generics allow us to create code that is flexible and can work with different types of data.
# They provide a way to define classes, functions, and data structures that can operate on any data type,
# without sacrificing type safety.

# In the example above, the 'Box' class is generic. It can hold any type of item, whether it's a string, integer, or any other type.
# This flexibility allows us to write code that is reusable and adaptable to different situations.

# While Python does not enforce generics at runtime, using type hints with generics provides valuable information to static type checkers,
# making it easier to catch potential type-related errors during development.

# Abstract classes and generics in Python provide a way to define common behavior and enforce type constraints in a flexible manner.
