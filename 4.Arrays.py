# Arrays in Python

# An array is a collection of elements that are stored at contiguous memory locations.
# It allows you to store multiple items of the same data type under a single name.

# Arrays in Python are implemented using the `list` type, which is a dynamic array.
# While not strictly a fixed-size array, Python lists can effectively serve similar purposes.

# Example:

# Creating an array (list) of integers
my_array = [1, 2, 3, 4, 5]

# Accessing elements in an array
first_element = my_array[0]  # Accessing the first element (index 0)
second_element = my_array[1]  # Accessing the second element (index 1)

# Modifying elements in an array
my_array[2] = 10  # Changing the third element to 10

# Getting the length of an array
array_length = len(my_array)

# Appending an element to the end of an array
my_array.append(6)

# Removing an element from an array
removed_element = my_array.pop(2)  # Remove and return element at index 2

# Slicing an array
subset = my_array[1:4]  # Get elements from index 1 to 3 (excluding 4)

# Checking if an element is in the array
element_exists = 3 in my_array

# Iterating over an array
for item in my_array:
    print(item)

# Arrays are versatile and can be used for various purposes, including storing collections of data,
# performing mathematical operations, and implementing algorithms.

# Related Functions:

# Sorting an array
# Creates a new sorted array, original array remains unchanged
sorted_array = sorted(my_array)
my_array.sort()  # Sorts the array in-place

# Reversing an array
# Creates a new reversed array, original array remains unchanged
reversed_array = list(reversed(my_array))
my_array.reverse()  # Reverses the array in-place

# Finding the maximum and minimum element in an array
max_value = max(my_array)
min_value = min(my_array)

# Getting the index of a specific element in an array
index_of_4 = my_array.index(4)

# Counting occurrences of an element in an array
count_of_2 = my_array.count(2)

# Removing the first occurrence of a specific element in an array
my_array.remove(2)

# Clearing all elements from an array
my_array.clear()

# Arrays in Python provide a flexible and powerful way to work with collections of data.
