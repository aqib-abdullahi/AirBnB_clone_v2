#!/usr/bin/python3

import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User

class TestFileStorage(unittest.TestCase):
    """
    class for testing FileStorage class' methods
    """
    temp_file = ""

    @staticmethod
    def move_file(src, dest):
        with open(src, 'r', encoding='utf-8') as myFile:
            with open(dest, 'w', encoding='utf-8') as tempFile:
                tempFile.write(myFile.read())
        os.remove(src)

    def setUp(self):
        self.temp_file = '/temp_store.json'
        self.temp_objs = [BaseModel(), BaseModel(), BaseModel()]
        for obj in self.temp_objs:
            storage.new(obj)
        storage.save()

    def tearDown(self):
        """initialized object
        """
        del self.temp_objs

    def test_type(self):
        """type checks for FileStorage
        """
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_save(self):
        """tests save functionality for FileStorage
        """
        with open('file.json', 'r', encoding='utf-8') as myFile:
            dump = myFile.read()
        self.assertNotEqual(len(dump), 0)
        temp_d = eval(dump)
        key = self.temp_objs[0].__class__.__name__ + '.'
        key += str(self.temp_objs[0].id)
        self.assertNotEqual(len(temp_d[key]), 0)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(temp_d[key2], KeyError)
        except:
            pass

    def test_reload(self):
        """tests reload functionality for FileStorage
        """
        storage.reload()
        obj_d = storage.all()
        key = self.temp_objs[1].__class__.__name__ + '.'
        key += str(self.temp_objs[1].id)
        self.assertNotEqual(obj_d[key], None)
        self.assertEqual(obj_d[key].id, self.temp_objs[1].id)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except:
            pass

    def test_delete_basic(self):
        """tests delete basic functionality for FileStorage
        """
        obj_d = storage.all()
        key2 = self.temp_objs[2].__class__.__name__ + '.'
        key2 += str(self.temp_objs[2].id)
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except:
            pass
