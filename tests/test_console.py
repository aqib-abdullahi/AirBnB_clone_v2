#!/usr/bin/python3
"""console test"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestConsole(unittest.TestCase):
    """this will test the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_create(self):
        """Test create command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create idan")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User email="user" password="passwd"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertEqual(
                "[\"[User", f.getvalue()[:7])

if __name__ == "__main__":
    unittest.main()
