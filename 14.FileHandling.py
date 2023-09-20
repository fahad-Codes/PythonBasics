# File Handling in Python

# File handling in Python allows you to perform operations on files, such as reading from or writing to them.

# Opening and Closing Files:

# Example 1: Opening a File

file_path = "sample.txt"

# 'open()' function is used to open a file.
# The first argument is the file path, and the second argument is the mode ('r' for read, 'w' for write, 'a' for append).
# By default, files are opened in text mode.

# Opening a file in read mode
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

# Explanation:
# - I've opened a file named "sample.txt" in read mode ('r').
# - 'with' statement ensures that the file is properly closed after use.
# - 'file.read()' reads the entire content of the file and assigns it to the variable 'content'.

# Example 2: Writing to a File

output_path = "output.txt"

# Opening a file in write mode
with open(output_path, 'w') as file:
    file.write("This is a test.")

# Explanation:
# - I've opened a file named "output.txt" in write mode ('w').
# - 'file.write()' writes the provided string to the file.

# Reading and Writing Modes:

# 'r': Open for reading (default).
# 'w': Open for writing, truncating the file first.
# 'a': Open for writing, appending to the end of the file.
# 'b': Binary mode.
# 't': Text mode (default).

# Reading from Files:

# Example 3: Reading Lines from a File

file_path = "sample.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Explanation:
# - I've opened the "sample.txt" file in read mode.
# - 'file.readlines()' returns a list of lines from the file.
# - I iterate over the lines and print them after stripping any trailing newline characters.

# Related Functions:

# - 'read()': Reads the entire content of the file.
# - 'readline()': Reads a single line from the file.
# - 'readlines()': Reads all lines and returns a list of strings.
# - 'write()': Writes a string to the file.
# - 'seek()': Moves the file pointer to a specified position.
# - 'tell()': Returns the current position of the file pointer.
# - 'close()': Closes the file.

# File handling is crucial for working with external data sources and is a fundamental skill for any programmer.
