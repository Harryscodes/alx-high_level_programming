#!/usr/bin/python3
"""
modules to test the base class and its methods
"""
import __init__ as pkg
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):

    """
    Test class for test cases for the Base class
    """

    @classmethod
    def setUpClass(self):
        """
        setup class method that runs first and just once
        until all test is completed

        initialises all needed attributes
        """
        b_obj = Base._Base__nb_objects
#        print(b_obj)
        b_tobj = Base._Base__true_nb_objects
        b_pro = Base._Base__properties

        if b_obj > 1:
            print("""
            Base testcase: previous Base counter not
            reset, now at: {}""".format(b_obj))

        if b_tobj > 1:
            print("""
            Base testcase: previous total Base counter
            not reset, now at: {}""".format(b_tobj))

        if len(b_pro) > 0:
            print("""
            Base testcase: previous Base ids still
            potentially in use: {}""".format(b_pro))

    def tearDown(self):
        """
        tearDown method that runs everytime a
        test is completed and

        Reinitializes obejct iterator and set of
        assigned properties.
        """
        b_pro = Base._Base__properties
        Base._Base__nb_objects = 0
        b_obj = Base._Base__nb_objects
        Base._Base__true_nb_objects = 0
        b_tobj = Base._Base__true_nb_objects
        b_pro.clear()

        if b_obj > 1:
            print("""
            Base testcase: Base counter not reset,
            now at: {}""".format(b_obj))

        if b_tobj > 1:
            print("""
            Base testcase: total Base counter not reset,
            now at: {}""".format(b_tobj))

        if len(b_pro) > 0:
            print("""
            Base testcase: Base properties still
            potentially in use: {}""".format(b_pro))

    def test_classAttribute(self):
        """
        test-cases to test for class attribute
        """
        self.assertEqual(0, Base._Base__nb_objects)
        self.baseobj = Base()
        self.assertEqual(1, Base._Base__nb_objects)
        self.newobj = Base()
        self.assertEqual(2, Base._Base__nb_objects)
        self.someobj = Base(13)
        self.assertEqual(2, Base._Base__nb_objects)

    def test_InstanceId(self):
        """
        test-cases to test for instance id
        """
        self.baseobj = Base()
        self.assertEqual(1, self.baseobj.id)
        self.newInstance = Base(12)
        self.assertEqual(12, self.newInstance.id)
        self.instance = Base()
        self.assertEqual(2, self.instance.id)

    def test_instanceIdLessThanzero(self):
        """
        test-case for instance id that is
        less than 0
        """
        with self.assertRaises(ValueError):
            obj = Base(-3)

    def test_toJsonString(self):
        """
        task 15 tests
        test-case to test the method
        to_json_string()
        """
        self.obj = Base()
        clas = self.obj.__class__.__name__
        t1 = [{'id': 3, 'class': 'Base'}]
        t1result = '[{"class": "Base", "id": 3}]'
        t2 = [{'count': 1, 'class': clas}, {'id': 45, 'fact': True}]
        t2result = '[{"class": "Base", "count": 1}, {"fact": true, "id": 45}]'
        json_str = self.obj.to_json_string(t1)
        self.assertEqual(t1result, json_str)
        json_str1 = self.obj.to_json_string(t2)
        self.assertEqual(t2result, json_str1)
        self.assertEqual('[]', self.obj.to_json_string([]))
        self.assertEqual('[]', self.obj.to_json_string(None))

    def test_saveToFile(self):
        """
        test-case to test the method
        save_to_file():
        """
        pass

    def test_fromJsonString(self):
        """
        Task 17 test case
        test-case to test the method
        from_json_string():
        """
        self.recInstance = Rectangle(2, 5)
        clas = self.recInstance.__class__.__name__
        t1 = '[{"id": 3, "class": "Rectangle"}]'
        t1result = [{"id": 3, 'class': 'Rectangle'}]
        t2 = '[{"class": "Rectangle"}, {"fact": true}]'
        t2result = [{'class': clas}, {'fact': True}]

        rv = self.recInstance.from_json_string(t1)
        rv2 = self.recInstance.from_json_string(t2)
        self.assertEqual(t1result, rv)
        self.assertEqual(t2result, rv2)
        """ test for empty string """
        self.assertEqual([], self.recInstance.from_json_string(''))
        """ test for None """
        self.assertEqual([], self.recInstance.from_json_string(None))


if __name__ == '__main__':
    unittest.main()
