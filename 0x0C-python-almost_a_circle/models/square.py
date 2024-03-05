#!/usr/bin/python3

"""
module that houses a class called Square
which inherits from another class called
Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that defines how a
    square is modelled. it inherits from
    the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        method to initialize a Square
        instance
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        method that defines what happens when python str()
        is called on a Square instance
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        getter method to get the public size attribute of Square instance
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method to set the public size attribute of Square instance
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0. Example: width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        public instance method that updates attributes
        of Square instance
        """
        if args:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if not isinstance(args[0], int):
                    raise TypeError("id must be an integer")
                setattr(self, attr[i], arg)
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
        all custom assigned attributes of Square instance
        """
        return {'x': self.x, 'y': self.y, 'size': self.size, 'id': self.id}

    def display(self):
        """
        public method to display # representation for Rectangle instance
        """
        super().display(size, size)
