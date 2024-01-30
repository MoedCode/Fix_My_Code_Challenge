#!/usr/bin/env python3
class Square:
    """A class representing a square with width and height attributes."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


# Creating an instance of Square with specific values
s1 = Square(width=5, height=5)

# Accessing class attributes directly
print("# Accessing class attributes directly")
print(Square.width, Square.height)  # Output: 0 0

# Accessing instance attributes
print("# Accessing instance attributes")
print(s1.width, s1.height)  # Output: 5 5

# Overwriting class attribute from the instance
s1.width = 10
s1.height = 8

# Accessing class attributes after overwriting
print("# Accessing class attributes after overwriting")
print(Square.width, Square.height)  # Output: 0 0

# Accessing instance attributes after overwriting
print("# Accessing instance attributes after overwriting")
print(s1.width, s1.height)  # Output: 10 8
