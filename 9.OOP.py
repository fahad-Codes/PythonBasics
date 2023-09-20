# Object-Oriented Programming (OOP) in Python

# OOP is a programming paradigm that allows us to organize code by modeling real-world entities as objects with attributes and behaviors.

# Pillars of OOP:
# 1. Encapsulation: Bundling data (attributes) and methods (functions) that operate on the data within a single unit (class).
# 2. Inheritance: Creating new classes (subclasses) based on existing classes (superclasses), inheriting their attributes and behaviors.
# 3. Polymorphism: The ability of a class to take on multiple forms. Methods can be overridden in subclasses to provide different implementations.
# 4. Abstraction: Simplifying complex systems by hiding the implementation details and exposing only the necessary parts.

# Example 1: Encapsulation

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating an instance of Person
person1 = Person("Alice", 30)

# Accessing attributes (encapsulation)
name = person1.name  # Result: "Alice"
age = person1.age  # Result: 30

# Calling a method (encapsulation)
person1.display_info()  # Output: "Name: Alice, Age: 30"

# Example 2: Inheritance


class Student(Person):  # Student inherits from Person
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the superclass
        self.student_id = student_id

    def display_info(self):  # Override display_info method
        print(
            f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")


# Creating an instance of Student
student1 = Student("Bob", 20, "12345")

# Accessing inherited attributes
student_name = student1.name  # Result: "Bob"
student_age = student1.age  # Result: 20

# Accessing subclass-specific attribute
student_id = student1.student_id  # Result: "12345"

# Calling overridden method (polymorphism)
student1.display_info()  # Output: "Name: Bob, Age: 20, Student ID: 12345"

# Example 3: Polymorphism


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Override area method for circles
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):  # Override area method for squares
        return self.side_length**2


# Creating instances of Circle and Square
circle1 = Circle(5)
square1 = Square(4)

# Calculating areas (polymorphism)
circle_area = circle1.area()  # Result: 78.5
square_area = square1.area()  # Result: 16

# Example 4: Abstraction


class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Balance: {self.balance}")


# Creating an instance of Bank
bank1 = Bank()

# Using abstraction to interact with the Bank object
bank1.deposit(1000)
bank1.withdraw(500)
bank1.display_balance()  # Output: "Balance: 500"

# Object-Oriented Programming (OOP) is a powerful paradigm for organizing code. It enhances code reusability, maintainability, and scalability by modeling real-world entities as objects.
