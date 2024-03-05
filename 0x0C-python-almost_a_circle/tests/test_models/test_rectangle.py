#!/usr/bin/python3
import __init__ as pkg
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


"""
modules to test the Rectangle class and its methods
"""


class TestRectangleClass(unittest.TestCase):
    """
    Class that test the Rectangle class
    and its associated methods
    """

    @classmethod
    def setUpClass(cls):
        """
        setUp class method that is ran first and just
        once until all test cases are completed
        """
        t_robj = Rectangle._Rectangle__true_nb_objects
        r_pro = Rectangle._Rectangle__properties
        b_nobj = Base._Base__nb_objects

        if t_robj > 0:
            print("""
            Total Rectangle instance as at now is
            {}""".format(t_robj))
        if len(r_pro) > 0:
            print("""
            some Rectangle instance still here: => {}
            """.format(r_pro))

    def setUp(self):
        """
        setUp method that runs everytime a test is executed
        """
        Base.resetclasspri_attr()

    def tearDown(self):
        """
        tearDown method that is executed everytime
        a test is completed.
        """
        t_robj = Rectangle._Rectangle__true_nb_objects
        b_nobj = Rectangle._Base__nb_objects
        r_pro = Rectangle._Rectangle__properties
        b_pro = Rectangle._Base__properties
        t_robj = 0
        b_nobj = 0
        r_pro.clear()
        b_pro.clear()

    def test_recAttribute(self):
        """ test to verify attribute """
        # create a Rectangle instance with 2 args
        self.obj = Rectangle(12, 35)
        # instance_id depends on Base private_attr __nb_objects
        self.assertEqual(Base._Base__nb_objects, self.obj.id)
        # test for instance width
        self.assertEqual(12, self.obj.width)
        # another instance of Rectangle with 5 args
        self.obj2 = Rectangle(3, 6, 1, 4, 10)
        # test for new instance id
        self.assertEqual(10, self.obj2.id)
        # test for new instance height
        self.assertEqual(6, self.obj2.height)
        # new instance with integer < 1 as 2nd arg
        with self.assertRaises(ValueError):
            Rectangle(3, 0, 5, 6, 7)

    def test_attributeTypes(self):
        """ test for attributes type """
        # negative integer as id
        with self.assertRaises(ValueError):
            obj = Rectangle(2, 3, 6, 5, -2)
        # 2 args with wrong data as first arg
        with self.assertRaises(TypeError):
            obj = Rectangle('2', 3)
        # 4 args with negative int for 3rd arg
        with self.assertRaises(ValueError):
            obj = Rectangle(2, 5, -1, 0)
        # 5 args with expected data type
        raw_obj = Rectangle(2, 5, 1, 4, 8)
        self.assertEqual(int, type(raw_obj.width))
        # 0 args
        with self.assertRaises(TypeError):
            Rectangle()
        # 5 args with wrong data type as first arg
        with self.assertRaises(TypeError):
            Rectangle(2.1, 4, 6, 12, 7)
        # 5 args with None as 2nd arg
        with self.assertRaises(TypeError):
            Rectangle(2, None, 8, 1, 9)

    def test_areaMethod(self):
        """ test for the area method """
        # create Rectangle instance with 2 args
        newInstance = Rectangle(3, 5)
        self.assertEqual(15, newInstance.area())
        # pass unwanted args to area method
        with self.assertRaises(TypeError):
            newInstance.area(7)

    def test_display(self):
        """ test for the display method """
        # create an instance of Rectangle with 5 args
        instance = Rectangle(3, 2, 2, 4, 1)
        # use patch to grab result printed in stdout
        with patch('sys.stdout', new=StringIO()) as output:
            instance.display()
            printed = output.getvalue().strip()
            self.assertEqual("###\n   ###", printed)

    def test__str__(self):
        """ test for the magic method __str__"""
        # create an instance of Rectangle with 5 args
        rec = Rectangle(4, 5, 6, 7, 7)
        # test for the string representation of rec instance
        self.assertEqual(str(rec), "[Rectangle](7) 6/7 - 4/5")
        # another instance of Rectangle with 2 args
        rec1 = Rectangle(6, 1)
        # test for the string representation of rec1 instance
        self.assertEqual(str(rec1), "[Rectangle](1) 0/0 - 6/1")
        # another instance of Rectangle with 3 args
        rec2 = Rectangle(6, 1, 5)
        # test for the string representation of rec2 instance
        self.assertEqual(str(rec2), "[Rectangle](2) 5/0 - 6/1")

    def test_update_posArgs(self):
        """ test for the update method with position args """
        # instance of Rectangle
        rec = Rectangle(3, 5)
        # test for current rec id using positional args
        self.assertEqual(1, rec.id)
        # update rec id
        rec.update(7)
        # test to confirm update
        self.assertEqual(7, rec.id)
        # update rec id and width
        rec.update(3, 5)
        # test to confirm new rec.id
        self.assertEqual(3, rec.id)
        # test to confirm new rec width
        self.assertEqual(5, rec.width)
        # test to verify data type
        with self.assertRaises(TypeError):
            rec.update(3, "2", 5)
        # test to verify the value passed
        with self.assertRaises(ValueError):
            rec.update(0, 0, 2, 5)
        # update rec id, width, height, x
        rec.update(4, 2, 8, 9)
        # test to verify rec y
        self.assertEqual(0, rec.y)
        # test to verify rec x
        self.assertEqual(9, rec.x)
        # test to verify rec id
        self.assertEqual(4, rec.id)
        # update rec id, width, height, x, y
        rec.update(1, 6, 8, 5, 3)
        # teat to verify rec y
        self.assertEqual(3, rec.y)

    def test_update_kwargs(self):
        """ test fot update method with keyword args """
        # create Rectangle instance
        rec = Rectangle(1, 2)
        # update rec using keyword arg
        rec.update(x=2, y=5)
        # test to verify rec x
        self.assertEqual(2, rec.x)
        # test to verify rec y
        self.assertEqual(5, rec.y)
        with self.assertRaises(TypeError):
            rec.update(width='3')
        with self.assertRaises(ValueError):
            rec.update(id=-1)
        self.assertEqual(1, rec.id)
        with self.assertRaises(TypeError):
            rec.update(id='4')

    def test_toDictionary(self):
        """ test for the to_dictionary representation method """
        rec = Rectangle(5, 7)
        attr = rec.to_dictionary()
        self.assertEqual(5, attr['width'])
        self.assertEqual(7, attr['height'])

    def test_toJsonString(self):
        """ test for the class method to_json_string """
        rec = Rectangle(6, 9)
        dl = Rectangle.to_json_string(rec.to_dictionary())
        str_dict = '{"x": 0, "width": 6, "id": 1, "height": 9, "y": 0}'
        self.assertEqual(dl, str_dict)
        dic = {'id': 2, 'width': 5}, {'x': 3, 'y': 7}
        dl = Rectangle.to_json_string([dic])
        self.assertEqual(dl, '[{"id": 2, "width": 5}, {"x": 3, "y": 7}]')
        # Empty list
        self.assertEqual(Base.to_json_string([]), '[]')
        # None list
        self.assertEqual(Base.to_json_string(None), '[]')
        # deprecated use: list not of dicts
        lst = [2, 3, 4]
        self.assertEqual(Base.to_json_string(lst), '[2, 3, 4]')
        # TypeError: no args
        self.assertRaises(TypeError, Base.to_json_string)
        dict_list = [{'width': 13, 'x': 5, 'height': 10, 'y': 11, 'id': 3}]
        # TypeError: testing with more than 1 arg
        with self.assertRaises(TypeError):
            Base.to_json_string(dict_list, dl)

    def test_saveToFile(self):
        """ test for method to save JSON string to file
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: list of `Rectangle` objects into JSON string file
        rec = Rectangle(5, 6, 7, 8, 9)
        Rectangle.save_to_file([])
        with open('Rectangle.json', encoding='utf-8') as file:
            contents = file.read()
        self.assertEqual(contents, '[]')
        # None list
        Rectangle.save_to_file(None)
        with open('Rectangle.json', encoding='utf-8') as file:
            contents = file.read()
        self.assertEqual(contents, '[]')
        # TypeError: arg not an iterable type
        self.assertRaises(TypeError, Rectangle.save_to_file, 5)
        # AttributeError: arg not a list, but tuple or set
        tup = (rec.to_dictionary(),)
        self.assertRaises(TypeError, Rectangle.save_to_file, tup)
        # AttributeError: list contents Base, not Square or Rectangle
        b1 = Base(3)
        self.assertRaises(AttributeError, Rectangle.save_to_file, [b1])
        # TypeError: no args
        self.assertRaises(TypeError, Rectangle.save_to_file)
        # TypeError: more than 1 arg
        self.assertRaises(TypeError, Rectangle.save_to_file, [rec], [tup])

    def test_from_json_string(self):
        """
        test for  method from_json_string to dictionary
        definition in `Base`, but tested here for inheritance.

        """
        # test for normal use: just 1 arg (str)
        j_str = '[{"width": 5, "height": 6, "x": 7, "y": 8, "id": 9}]'
        rec = Rectangle.from_json_string(j_str)
        list_dic = [{'width': 5, 'height': 6, 'x': 7, 'y': 8, 'id': 9}]
        self.assertEqual(rec, list_dic)
        # Test for empty string
        b = Rectangle.from_json_string('')
        self.assertEqual(b, [])
        list_dict = '[{"a": 2, "b": 5}, {"c": 12, "d": 3 }]'
        result = Rectangle.from_json_string(list_dict)
        self.assertEqual(result, [{'a': 2, 'b': 5}, {'c': 12, 'd': 3}])

    def test_create(self):
        """ test for the method create """
        dic = {'x': 3, 'y': 2, 'id': 6, 'width': 5, 'height': 4}
        rec = Rectangle.create(**dic)
        self.assertTrue(isinstance(rec, Rectangle))
        self.assertEqual(rec.id, 6)
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 4)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 2)
        # TypeError: no args
        self.assertRaises(TypeError, Rectangle.create)
        # TypeError: with fixed amount of non-keyword args
        self.assertRaises(TypeError, Rectangle.create, dic)
        # TypeError: with variable amount of non-keyword args
        self.assertRaises(TypeError, Rectangle.create, *dic)
        # KeyError: dict has bad key
        dic2 = {'area': 5, 'height': 6, 'x': 7, 'y': 8, 'id': 9}
        with self.assertRaises(TypeError):
            Rectangle.create(**dic2)
        # TypeError: dict has too many keys
        dic3 = {'area': 10, 'width': 5, 'height': 6, 'x': 7, 'y': 8, 'id': 9}
        self.assertRaises(TypeError, Rectangle.create, **dic3)
        # TypeError: dict has no keys
        dic4 = dict()
        self.assertRaises(TypeError, Rectangle.create, **dic4)

    def test_load_from_file(self):
        """ test for method load_from_file File to instances
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: file with JSON string of instances as dicts
        rec = Rectangle(10, 7, 2, 8)
        l_in = [rec]
        Rectangle.save_to_file(l_in)
        l_out = Rectangle.load_from_file()
        self.assertEqual(l_in[0].id, l_out[0].id)
        self.assertEqual(l_in[0].height, l_out[0].height)
        self.assertFalse(l_in[0] is l_out[0])
        self.assertNotEqual(id(l_in[0]), id(l_out[0]))
        self.assertEqual(l_in[0].x, l_out[0].x)
        self.assertEqual(l_in[0].y, l_out[0].y)
        self.assertEqual(l_in[0].width, l_out[0].width)
        # empty file returns empty list
        Rectangle.save_to_file(None)
        l_out = Rectangle.load_from_file()
        self.assertEqual(l_out, [])
        # empty list in file returns empty list
        Rectangle.save_to_file([])
        l_out = Rectangle.load_from_file()
        self.assertEqual(l_out, [])
        # file not found returns empty list
        emp = Rectangle.load_from_file()
        self.assertEqual(emp, [])


if __name__ == '__main__':
    unittest.main()
