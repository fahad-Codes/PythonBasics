# Loops and Related Functions in Python

# Loops are control structures that allow you to repeatedly execute a block of code.
# They are essential for tasks that require repetitive operations.

# Example 1: While Loop

# While Loop:
# The while loop repeatedly executes a block of code as long as a condition is true.

# Example:
x = 0
while x < 5:
    print(x)
    x += 1

# Explanation:
# - In this example, the while loop checks if x is less than 5. If true, it executes the indented block of code.
# - Inside the loop, x is printed and then incremented by 1.
# - This continues until x is no longer less than 5.

# Example 2: For Loop

# For Loop:
# The for loop iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each element.

# Example:
for i in range(5):
    print(i)

# Explanation:
# - In this example, the for loop iterates over the range of numbers from 0 to 4 (exclusive).
# - For each iteration, the current value of i is printed.

# Related Function: range()

# The range() function generates a sequence of numbers and is often used with for loops.

# Example:
for i in range(2, 10, 2):
    print(i)

# Explanation:
# - This for loop uses range(2, 10, 2), which generates numbers starting from 2, up to (but not including) 10, with a step of 2.
# - The loop will print 2, 4, 6, and 8.

# Example 3: Nested Loops

# Nested Loops:
# You can have loops inside loops, known as nested loops.

# Example:
for i in range(3):
    for j in range(2):
        print(i, j)

# Explanation:
# - In this example, there are two nested for loops. The outer loop iterates over the range of numbers from 0 to 2.
# - For each iteration of the outer loop, the inner loop iterates over the range of numbers from 0 to 1.
# - The combination of i and j is printed for each iteration of the inner loop.

# Related Function: break

# The break statement is used to exit a loop prematurely.

# Example:
for i in range(5):
    if i == 3:
        break
    print(i)

# Explanation:
# - In this example, the for loop iterates over the range of numbers from 0 to 4.
# - When i becomes 3, the if condition is true and the break statement is executed, exiting the loop.

# Related Function: continue

# The continue statement is used to skip the rest of the loop body for the current iteration.

# Example:
for i in range(5):
    if i == 3:
        continue
    print(i)

# Explanation:
# - In this example, the for loop iterates over the range of numbers from 0 to 4.
# - When i becomes 3, the if condition is true and the continue statement is executed, skipping the rest of the loop body for that iteration.

# Related Function: else in Loops

# The else block can be used with loops to execute code if the loop completes without encountering a break statement.

# Example:
for i in range(5):
    print(i)
else:
    print("Loop completed without a break")

# Explanation:
# - In this example, the for loop iterates over the range of numbers from 0 to 4.
# - After all iterations are completed, the else block is executed, printing "Loop completed without a break".

# Loops in Python are powerful tools for automating repetitive tasks, and they can be combined with related functions for even greater functionality.
