#!/usr/bin/python3
""" Write a class that defines a rectangle """


class Rectangle:
    """
    Class rectangle that defines a rectangle:
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes method for Rectangle
        Args:
        -Private instance attribute: width
        -Private instance attribute: height
        -Public instance method: def area(self)
        -Public instance method: def perimeter(self)
        -print() and str() should print the rectangle
        with the character #
        -repr() should return a string representation
        of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        str method for print the rectangle with #
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        repr method for representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print message when instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Private instance height of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Private instance height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Method to compare 2 rectangles
            rect_1 (class Rectangle): Rectangle 1 must be an instance rectangle
            rect_2 (class Rectangle): Rectangle 2 must be an instance rectangle
        Returns:
            The biggest rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Class method that defines a square
            cls : The parameter that points to the class
            size (int): The size of the square
        Returns:
            width = height = size
        """
        return cls(size, size)
