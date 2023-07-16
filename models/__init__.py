#!/usr/bin/python3
"""This module instantiates an object in the different storages"""
import os

type_storage = os.getenv('HBNB_TYPE_STORAGE')

if type_storage == 'db':
    from models.engine.file_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
