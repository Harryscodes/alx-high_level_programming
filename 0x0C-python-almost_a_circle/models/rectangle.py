#!/usr/bin/python3

"""
module to house a class called Rectangle
inheriting from the base class Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from
    the base class
    """
    __properties = {}
    __true_nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialises Rectangle instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        key = str(Rectangle.__true_nb_objects)
        clas = self.__class__.__name__
        baseclass = self.__class__.__base__.__name__
        Rectangle.__true_nb_objects += 1
        Rectangle.__properties[key] = self.__dict__
        Rectangle.__properties[key]["class"] = clas
        Rectangle.__properties[key]["baseclass"] = baseclass

    @property
    def width(self):
        """ getter method for private width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for private width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for private height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for private height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter method for private x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for private x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter method for private y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for private y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ public method for computation of area for Rectangle instance """
        return self.width * self.height

    def display(self):
        """
        public method to display # representation for Rectangle instance
        """
        rec = ''
        for j in range(self.y):
            print("", end="")
        for i in range(self.height):
            if i != self.height - 1:
                rec += '{} {}\n'.format(' ' * self.x, '#' * self.width)
            else:
                rec += '{} {}'.format(' ' * self.x, '#' * self.width)
        print(rec)

    def __str__(self):
        """
        method that defines what happens when python str()
        is called on a Rectangle instance
        """
        clas = f'[{self.__class__.__name__}]'
        idxy = f' ({self.id}) {self.x}/{self.y}'
        return clas + idxy + f' - {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """
        public instance method that updates attributes
        of Rectangle instance
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for ind, arg in enumerate(args):
                if not isinstance(args[0], int):
                    raise TypeError("id must be an integer")
                if args[0] < 0:
                    raise ValueError("id must be >= 0")
                setattr(self, attrs[ind], arg)
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    if not isinstance(v, int):
                        raise TypeError("id must be an integer")
                    if v < 0:
                        raise ValueError("id must be >= 0")
                setattr(self, k, v)

    def to_dictionary(self):
        """
        public instance method that returns a dictionary copy of
        all custom assigned attributes of Rectangle instance
        """
        y, x = self.y, self.x
        width, height = self.width, self.height
        id = self.id
        return {'x': x, 'width': width, 'id': id, 'height': height, 'y': y}
