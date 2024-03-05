#!/usr/bin/python3

"""module that houses a class Rectangle """


class Rectangle:
    """ a class that defines a rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initializes all instances of this class """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ to be called when an instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ getter for width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width property """
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height property """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method to calculate the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ method to calculate the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """ method that decides what to be printed
        when print is called on an instance of this class """

        if self.width == 0 or self.height == 0:
            return ""
        else:
            rec = ""
            for i in range(self.height):
                if i < self.height - 1:
                    rec += f"{str(self.print_symbol) * self.width}\n"
                else:
                    rec += "{}".format(str(self.print_symbol) * self.width)
            return rec

    def __repr__(self):
        """The python representation of what to be printed """
        return f"{self.__class__.__name__}({self.width}, {self.height})"
