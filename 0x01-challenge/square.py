#!/usr/bin/python3
""" Square module. """


class Square():
    """A class representing a square with width and height attributes."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize the Square with specified width and height."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Calculate the area of the square."""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Calculate the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the square's dimensions."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create Square instance """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
