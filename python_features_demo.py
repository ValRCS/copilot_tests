# We would like to write a short demonstration of the features of Python

# 1. Variables
# 2. Data types
# 3. Operators
# 4. Control structures
# 5. Functions
# 6. Classes
# 7. Modules
# 8. Packages
# 9. Exceptions
# 10. File handling
# 11. Regular expressions
# 12. JSON
# 13. Date and time
# 14. Math
# 15. Random
# 16. Statistics
# 17. Collections
# 18. Itertools
# 19. Threading
# 20. Multiprocessing

# 1. Variables
# Variables are used to store data in memory
# Variables can be of any type
# Variables can be assigned to other variables
# Variables can be reassigned to other values
# Variables can be reassigned to other types

# 2. Data types
# Python has several built-in data types
# int, float, str, bool, list, tuple, dict, set, frozenset, bytes, bytearray, memoryview, complex, range, None
# We can check the type of a variable using the type() function
# We can convert between types using the int(), float(), str(), bool(), list(), tuple(), dict(), set(), frozenset(), bytes(), bytearray(), memoryview(), complex(), range(), None() functions

# 3. Operators
# Python has several built-in operators
# Arithmetic operators: +, -, *, /, //, %, **
# Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Identity operators: is, is not
# Membership operators: in, not in
# Bitwise operators: &, |, ^, ~, <<, >>

# 4. Control structures
# Python has several built-in control structures
# if, elif, else
# for, while
# break, continue, pass

# 5. Functions
# Functions are used to group code that performs a specific task
# Functions can be called from other functions
# Functions can be called from other files
# Functions can be passed arguments
# Functions can return values

# 6. Classes
# Classes are used to group data and functions that perform a specific task
# Classes can be instantiated
# Classes can be inherited
# Classes can be passed arguments
# Classes can return values

# 7. Modules
# Modules are used to group code that performs a specific task
# Modules can be imported into other modules
# Modules can be imported into other files
# Modules can be passed arguments
# Modules can return values

# 8. Packages
# Packages are used to group modules that perform a specific task
# Packages can be imported into other modules
# Packages can be imported into other files
# Packages can be passed arguments
# Packages can return values

# 9. Exceptions
# Exceptions are used to handle errors
# Exceptions can be raised
# Exceptions can be caught
# Exceptions can be handled

# 10. File handling
# Files are used to store data on disk
# Files can be opened
# Files can be read
# Files can be written
# Files can be closed

# 11. Regular expressions
# Regular expressions are used to match patterns in strings
# Regular expressions can be compiled
# Regular expressions can be matched
# Regular expressions can be searched
# Regular expressions can be replaced

# 12. JSON
# JSON is used to store data in a human-readable format
# JSON can be encoded
# JSON can be decoded

# 13. Date and time
# Date and time are used to store dates and times
# Date and time can be formatted
# Date and time can be parsed

# 14. Math
# Math is used to perform mathematical operations
# Math can be used to calculate the absolute value
# Math can be used to calculate the ceiling
# Math can be used to calculate the floor
# Math can be used to calculate the factorial
# Math can be used to calculate the greatest common divisor
# Math can be used to calculate the least common multiple
# Math can be used to calculate the logarithm
# Math can be used to calculate the power
# Math can be used to calculate the square root
# Math can be used to calculate the trigonometric functions

# 15. Random
# Random is used to generate random numbers
# Random can be used to generate random numbers

# 16. Statistics
# Statistics is used to perform statistical operations
# Statistics can be used to calculate the mean
# Statistics can be used to calculate the median
# Statistics can be used to calculate the mode
# Statistics can be used to calculate the standard deviation
# Statistics can be used to calculate the variance

# 17. Collections
# Collections are used to store collections of data
# Collections can be used to store collections of data

# 18. Itertools
# Itertools are used to iterate over collections of data
# Itertools can be used to iterate over collections of data

# 19. Threading
# Threading is used to run multiple threads of execution
# Threading can be used to run multiple threads of execution

# 20. Multiprocessing
# Multiprocessing is used to run multiple processes
# Multiprocessing can be used to run multiple processes


# 1. Variables
# Variables are used to store data
# Variables can be used to store different types of data
# Variables can be used to store numbers
# Variables can be used to store strings
# Variables can be used to store boolean values
# Variables can be used to store lists
# Variables can be used to store dictionaries

# Example of using variables in Python
name = "Valdis"
age = 49
is_male = True
height = 1.81
interests = ["coding", "reading", "chess"]
person = {"name": name, "age": age, "is_male": is_male, "height": height, "interests": interests}

print("Name:", name)
print("Age:", age)
print("Is male:", is_male)
print("Height:", height)
print("Interests:", interests)
print("Person:", person)

# Example of using variables to hold sets, tuples, and None in Python
my_set = {1, 2, 3, 4, 5}
my_tuple = (6, 7, 8, 9, 10)
my_none = None

print("Set:", my_set)
print("Tuple:", my_tuple)
print("None:", my_none)

# Example of using variables to hold bytes, bytearrays, memoryviews, and complex numbers in Python
my_bytes = b"Hello"
my_bytearray = bytearray(5)
my_memoryview = memoryview(my_bytes)
my_complex = 1 + 2j

print("Bytes:", my_bytes)
print("Bytearray:", my_bytearray)
print("Memoryview:", my_memoryview)
print("Complex:", my_complex)

# Example of using variables to hold ranges in Python
my_range = range(5)

print("Range:", my_range)
# range is not a list, but it can be converted to a list
print("Range as list:", list(my_range))


# 2. Data types
# Python has several built-in data types
# int, float, str, bool, list, tuple, dict, set, frozenset, bytes, bytearray, memoryview, complex, range, None
# We can check the type of a variable using the type() function
# We can convert between types using the int(), float(), str(), bool(), list(), tuple(), dict(), set(), frozenset(), bytes(), bytearray(), memoryview(), complex(), range(), None() functions

# Example of using the type() function in Python
print("Type of name:", type(name))

# Example of using the int() function in Python
print("Int of 1.81:", int(1.81))

# Example of using the float() function in Python
print("Float of 49:", float(49))

# Example of using the str() function in Python
print("Str of 49:", str(49))

# Example of using the bool() function in Python
print("Bool of 49:", bool(49))

# Example of using the list() function in Python
print("List of 49:", list((49,50)))

# Example of using the tuple() function in Python
print("Tuple of 49:", tuple([49,2]))

# Example of using the dict() function in Python
print("Dict of 49:", dict([(49,50),(51,52)]))

# Example of using the set() function in Python
print("Set of 49:", set([3,2,4,1,2,2,1]))

# Example of using the frozenset() function in Python
print("Frozenset of 49:", frozenset([3,2,4,1,2,2,1]))

# Example of using the bytes() function in Python
print("Bytes of 49:", bytes(49))
print("Bytes of 49:", bytes("Valldis ar kaķiem un suņiem", "utf-8"))
# list of bytes(ascii) from string
print("Bytes of 49:", list(bytes("Valldis ar kaķiem un suņiem", "utf-8")))
print("Bytes of 49:", list(bytes("ā", "utf-8")))
# ord of ā
print("Bytes of 49:", ord("ā"))
# how does Unicode of 257 for ā convert to 196, 129 in bytes?
print("Bytes of 49:", bytes('ā', 'utf-8'))
# from https://www.johndcook.com/blog/2019/09/09/how-utf-8-works/
# So multibyte sequences have one of the following forms.

    # 110xxxxx 10xxxxxx
    # 1110xxxx 10xxxxxx 10xxxxxx
    # 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

# print bit view of 196
print("Bytes of 49:", bin(196))
# print bit view of 129
print("Bytes of 49:", bin(129))

# print number from last 5 bits of 196
print("Bytes of 49:", int(bin(196)[-5:], 2))
# print number from last 6 bits of 129
print("Bytes of 49:", int(bin(129)[-6:], 2))

# combine last 5 bits of 196 and last 6 bits of 129
print("Bytes of 49:", bin(196)[-5:] + bin(129)[-6:])
# convert that to decimal
print("Bytes of 49:", int(bin(196)[-5:] + bin(129)[-6:], 2))
# assert that to be 257
assert int(bin(196)[-5:] + bin(129)[-6:], 2) == 257



# # Example of using the bytearray() function in Python
# print("Bytearray of 49:", bytearray(49))

# # Example of using the memoryview() function in Python
# print("Memoryview of 49:", memoryview(b"49"))

