#!/usr/bin/python3
'''Module for Rectangle class.'''


class Rectangle:
    '''This class defines a simple Rectangle.'''

    number_of_instances = 0
    '''int: The number of active instances.'''

    print_symbol = '#'
    '''type: Print symbol, can be any type.'''

    def __init__(self, width=0, height=0):
        '''Constructor.
        Args:
            width: The width of rectangle.
            height: The height of rectangle.
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i != (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """genrating who is bigger

        Args:
            rect_1 (Rectangle): first argument
            rect_2 (Rectangle): second argument

        Raises:
            TypeError: if not from the same class
            TypeError: if not from the same class

        Returns:
            Rectangle: the bigger
        """
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
