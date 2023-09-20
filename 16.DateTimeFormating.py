# Date/Time Formatting in Python

# Python provides the 'datetime' module for working with dates and times.

# Example 1: Importing the datetime Module

import datetime

# Creating a Date Object:

# Example 2: Creating a Date Object

date = datetime.date(2022, 9, 18)

# Explanation:
# - I've created a date object representing September 18, 2022.

# Example 3: Getting the Current Date

current_date = datetime.date.today()

# Explanation:
# - 'datetime.date.today()' returns the current date.

# Date Formatting:

# Example 4: Formatting Dates

formatted_date = current_date.strftime("%Y-%m-%d")

# Result: "2022-09-18"

# Explanation:
# - I've used the 'strftime' method to format the date.
# - %Y: Year with century as a decimal number.
# - %m: Month as a zero-padded decimal number.
# - %d: Day of the month as a zero-padded decimal number.

# Creating a Time Object:

# Example 5: Creating a Time Object

time = datetime.time(14, 30, 0)

# Explanation:
# - I've created a time object representing 2:30 PM.

# Example 6: Getting the Current Time

current_time = datetime.datetime.now().time()

# Explanation:
# - 'datetime.datetime.now()' returns the current date and time.
# - 'time()' extracts the time part.

# Time Formatting:

# Example 7: Formatting Times

formatted_time = current_time.strftime("%H:%M:%S")

# Result: "14:30:00"

# Explanation:
# - I've used the 'strftime' method to format the time.
# - %H: Hour (24-hour clock) as a zero-padded decimal number.
# - %M: Minute as a zero-padded decimal number.
# - %S: Second as a zero-padded decimal number.

# Creating a DateTime Object:

# Example 8: Creating a DateTime Object

dt = datetime.datetime(2022, 9, 18, 14, 30, 0)

# Explanation:
# - I've created a datetime object representing September 18, 2022, 2:30 PM.

# Example 9: Getting the Current DateTime

current_datetime = datetime.datetime.now()

# Explanation:
# - 'datetime.datetime.now()' returns the current date and time.

# DateTime Formatting:

# Example 10: Formatting DateTimes

formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Result: "2022-09-18 14:30:00"

# Explanation:
# - I've used the 'strftime' method to format the datetime.

# Related Functions:

# - strptime(): Parses a string representing a date and time into a datetime object.
# - timedelta(): Represents the difference between two dates or times.

# The 'datetime' module provides powerful tools for working with dates and times in Python.
