class Rectangle:
    """This module defines a Rectangle class."""

    def __init__(self, width=0, height=0):
        """Represent a rectangle."""
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    def __repr__(self):
        """Return a string representation of the Rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle."""
        return 2 * (self.width + self.height)
