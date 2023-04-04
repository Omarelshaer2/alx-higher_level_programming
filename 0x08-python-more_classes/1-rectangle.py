class Rectangle:
    """
    Represents a rectangle shape with a width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle object with optional width and height.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Retrieves the width of the Rectangle object.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle object to the given value.
        Raises a TypeError exception if value is not an integer.
        Raises a ValueError exception if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be >= 0.")
        self._width = value

    @property
    def height(self):
        """
        Retrieves the height of the Rectangle object.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle object to the given value.
        Raises a TypeError exception if value is not an integer.
        Raises a ValueError exception if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be >= 0.")
        self._height = value
