# Lists, Tuples, Sets, and Dictionaries in Python

# Lists:
# Lists are ordered collections of items. They can contain elements of different types and can be modified.

# Example 1: Creating and Manipulating Lists

# Create a list
fruits = ['apple', 'banana', 'cherry']

# Accessing elements
first_fruit = fruits[0]  # Result: 'apple'
last_fruit = fruits[-1]  # Result: 'cherry'

# Modifying a list
fruits.append('date')  # Adds 'date' to the end of the list

# Removing an element
# Removes and returns the element at index 1 ('banana')
removed_fruit = fruits.pop(1)

# Length of the list
num_fruits = len(fruits)  # Result: 3

# Tuples:
# Tuples are similar to lists, but they are immutable (cannot be changed).

# Example 2: Creating and Accessing Tuples

# Create a tuple
coordinates = (3, 5)

# Accessing elements
x = coordinates[0]  # Result: 3
y = coordinates[1]  # Result: 5

# Trying to modify a tuple (will raise an error)
# coordinates[0] = 4  # This line will cause an error

# Sets:
# Sets are unordered collections of unique elements.

# Example 3: Creating and Manipulating Sets

# Create a set
colors = {'red', 'green', 'blue', 'red'}  # 'red' is only included once

# Adding an element
colors.add('yellow')

# Removing an element
colors.remove('green')

# Checking membership
is_yellow_present = 'yellow' in colors  # Result: True

# Length of the set
num_colors = len(colors)  # Result: 3

# Dictionaries:
# Dictionaries are collections of key-value pairs. They are unordered and can be modified.

# Example 4: Creating and Accessing Dictionaries

# Create a dictionary
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Accessing values
person_name = person['name']  # Result: 'Alice'
person_age = person.get('age')  # Result: 30

# Modifying a dictionary
person['age'] = 31

# Adding a new key-value pair
person['occupation'] = 'Engineer'

# Removing a key-value pair
# Removes and returns the value associated with 'city' key
removed_city = person.pop('city')

# Checking if a key exists
is_occupation_present = 'occupation' in person  # Result: True

# Length of the dictionary
num_properties = len(person)  # Result: 3

# Related Functions:

# list(): Converts an iterable to a list.
numbers_list = list(range(5))  # Result: [0, 1, 2, 3, 4]

# tuple(): Converts an iterable to a tuple.
numbers_tuple = tuple(range(5))  # Result: (0, 1, 2, 3, 4)

# set(): Converts an iterable to a set.
numbers_set = set(range(5))  # Result: {0, 1, 2, 3, 4}

# dict(): Creates a dictionary from a sequence of key-value pairs.
# Result: {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}
person_dict = dict(name='Bob', age=25, city='San Francisco')

# Explaining Sets:
# Sets are unordered collections of unique elements. They are useful for tasks like finding unique items in a list or performing set operations (intersection, union, etc.).
# Example 5: Set Operations

# Create sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Intersection of sets
intersection = set1.intersection(set2)  # Result: {4, 5}

# Union of sets
union = set1.union(set2)  # Result: {1, 2, 3, 4, 5, 6, 7, 8}

# Difference of sets
difference = set1.difference(set2)  # Result: {1, 2, 3}

# Symmetric difference of sets
symmetric_difference = set1.symmetric_difference(
    set2)  # Result: {1, 2, 3, 6, 7, 8}

# Explaining Dictionaries:
# Dictionaries store data in key-value pairs, providing fast lookup for values based on their keys. They are versatile and widely used in various applications.
# Example 6: Dictionary Operations

# Create a dictionary
grades = {'Alice': 85, 'Bob': 70, 'Charlie': 95}

# Accessing values
bob_grade = grades['Bob']  # Result: 70

# Adding a new entry
grades['David'] = 75

# Removing an entry
# Removes and returns the grade associated with 'Charlie'
removed_charlie_grade = grades.pop('Charlie')

# Checking if a student is in the dictionary
is_eve_present = 'Eve' in grades  # Result: False

# Getting a list of keys
student_names = list(grades.keys())  # Result: ['Alice', 'Bob', 'David']

# Getting a list of values
student_grades = list(grades.values())

# Result: [85, 70, 75]

# Getting a list of key-value pairs (tuples)
# Result: [('Alice', 85), ('Bob', 70), ('David', 75)]
grade_items = list(grades.items())

# Length of the dictionary
num_students = len(grades)  # Result: 3

# Lists, Tuples, Sets, and Dictionaries are fundamental data structures in Python, each with their own characteristics and use cases.
