# Regular Expressions (Regex) in Python

# Regular expressions are sequences of characters that define a search pattern. They are used for pattern matching within strings.

# Example 1: Matching Patterns

import re

# Define a pattern
pattern = r'hello'

# Define a string
text = 'hello world'

# Using re.search() to find a match
match = re.search(pattern, text)

if match:
    print(f'Match found: {match.group()}')
else:
    print('No match')

# Explanation:
# - In this example, we define a pattern 'hello' using a raw string (r'hello').
# - We define a text string 'hello world'.
# - We use `re.search()` to search for the pattern within the text.
# - If a match is found, it prints the matched string using `match.group()`.
# - In this case, it would print: "Match found: hello".

# Example 2: Using Metacharacters

pattern = r'\d+'  # Match one or more digits

text = 'There are 123 apples and 456 oranges.'

matches = re.findall(pattern, text)

print(matches)  # Output: ['123', '456']

# Explanation:
# - In this example, we define a pattern '\d+'.
# - '\d' is a metacharacter that matches any digit. '+' matches one or more occurrences.
# - We define a text string containing numbers.
# - We use `re.findall()` to find all occurrences of the pattern in the text.
# - It returns a list of matched strings.

# Example 3: Using Groups

pattern = r'(\d{3})-(\d{2})-(\d{4})'  # Match a date in format: XXX-XX-XXXX

text = 'Date of birth: 123-45-6789'

match = re.search(pattern, text)

if match:
    print(f'Date found: {match.group()}')
    print(
        f'Year: {match.group(3)}, Month: {match.group(2)}, Day: {match.group(1)}')
else:
    print('Date not found')

# Explanation:
# - In this example, we define a pattern with groups for year, month, and day.
# - '(\d{3})' matches three digits (year), '(\d{2})' matches two digits (month), and '(\d{4})' matches four digits (day).
# - We define a text string containing a date.
# - We use `re.search()` to search for the pattern within the text.
# - If a match is found, it prints the matched date and extracts the year, month, and day using `match.group()`.

# Related Functions:

# re.findall(): Finds all occurrences of a pattern in a string and returns them as a list.
# re.match(): Matches a pattern at the beginning of a string. Returns a match object if successful.
# re.fullmatch(): Matches the entire string against the pattern. Returns a match object if successful.
# re.sub(): Replaces occurrences of a pattern with a specified string.
# re.compile(): Compiles a regular expression pattern into a regular expression object.

# Regular expressions provide a powerful tool for pattern matching and text manipulation in Python.
