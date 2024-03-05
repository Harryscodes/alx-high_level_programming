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
        """The python representation of what to be printed

        Args:
            self: reference to an instance of the class Rectangle

        Return:
              The python representation of the Rectangle class
        """
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method that compares and returns
        biggest rectangle based on the area

        Args:
            rect_1: first Rectangle object
            rect_2: second Rectangle object

        Return:
              the object with the biggest area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        biggest = rect_1 if rect_1.area() >= rect_2.area() else rect_2
        return biggest

    @classmethod
    def square(cls, size=0):
        """ class method that returns a Rectangle
        instance as square

        Args:
            cls: reference to the class itself
            size: size of the square sides

        Return:
            an instance of the class wuith the size as sides
        """
        return cls(size, size)
