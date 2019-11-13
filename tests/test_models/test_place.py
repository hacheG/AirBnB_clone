#!/usr/bin/python3
"""Unittests for base model class"""


import unittest
from models.place import Place
from datetime import datetime
from uuid import UUID
from models import storage


class TestsBaseModel(unittest.TestCase):

    def test_normal_cases_place(self):
        """normal cases"""
        my_object = Place()
        my_object.name = "Holbiland"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "Holbiland")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "Place")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)