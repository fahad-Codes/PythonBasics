# Python Strings

# Strings in Python are sequences of characters, and they are a fundamental data type in Python.

# Example 1: Creating a String

# Strings can be created using single, double, or triple quotes.
single_quoted_string = 'Hello, World!'
double_quoted_string = "Python"
triple_quoted_string = '''This is a multi-line string.
It can span multiple lines.'''

# Explanation:
# - I've created three strings using single, double, and triple quotes respectively.
# - Triple-quoted strings can span multiple lines.

# String Concatenation:

# Example 2: Concatenating Strings

first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name

# Result: "John Doe"

# Explanation:
# - I've concatenated the strings "John" and "Doe" along with a space.

# String Indexing and Slicing:

# Example 3: Indexing and Slicing

message = "Hello, Python"

first_character = message[0]  # Result: 'H'
substring = message[7:13]  # Result: 'Python'

# Explanation:
# - I've used indexing to get the first character of the string.
# - I've used slicing to extract the substring "Python".

# String Methods:

# Example 4: Using String Methods

text = "   Python is fun!   "
stripped_text = text.strip()  # Removes leading and trailing spaces

lowercase_text = text.lower()  # Converts to lowercase
uppercase_text = text.upper()  # Converts to uppercase

replaced_text = text.replace("fun", "awesome")  # Replaces 'fun' with 'awesome'

# Explanation:
# - I've used various string methods to manipulate the text.
# - 'strip()' removes leading and trailing spaces.
# - 'lower()' converts the string to lowercase.
# - 'upper()' converts the string to uppercase.
# - 'replace()' replaces occurrences of a substring.

# String Formatting:

# Example 5: String Formatting

name = "Alice"
age = 30

formatted_string = f"My name is {name} and I am {age} years old."

# Result: "My name is Alice and I am 30 years old."

# Explanation:
# - I've used f-strings to format the string with variables.

# Related Functions:

# - len(): Returns the length of a string.
# - split(): Splits a string into a list of substrings based on a delimiter.
# - join(): Joins a list of strings into a single string using a specified delimiter.

# Strings are a versatile data type in Python and are used extensively for text processing and manipulation.
