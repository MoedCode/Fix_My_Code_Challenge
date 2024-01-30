#!/usr/bin/python3
#!/usr/bin/python3

class Square():
    """A class representing a square with width and height attributes."""

    def __init__(self, *args, **kwargs):
        """Initialize the Square with specified width and height."""
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """perimeter of the square."""
        return self.width * 4

    def __str__(self):
        """String representation of the square's dimensions."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
