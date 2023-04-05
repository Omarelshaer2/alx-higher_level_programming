class Rectangle:
    """
    A 2D rectangle with width and height attributes.
    """
    def __init__(self, w=0, h=0):
        """
        Initializes a Rectangle object with width w and height h.
        """
        self.w, self.h = w, h

    @property
    def w(self):
        """
        The width of the rectangle.
        """
        return self.__w

    @w.setter
    def w(self, v):
        """
        Set the width of the rectangle to v.
        """
        if type(v) is not int:
            raise TypeError("Width must be an integer")
        if v < 0:
            raise ValueError("Width must be non-negative")
        self.__w = v

    @property
    def h(self):
        """
        The height of the rectangle.
        """
        return self.__h

    @h.setter
    def h(self, v):
        """
        Set the height of the rectangle to v.
        """
        if type(v) is not int:
            raise TypeError("Height must be an integer")
        if v < 0:
            raise ValueError("Height must be non-negative")
        self.__h = v

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__w * self.__h

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        if self.__w == 0 or self.__h == 0:
            return 0
        return (self.__w * 2) + (self.__h * 2)

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        return "\n".join("#" * self.__w for _ in range(self.__h))
