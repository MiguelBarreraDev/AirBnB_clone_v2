#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

config = {
    "user": getenv("HBNB_MYSQL_USER"),
    "passwd": getenv("HBNB_MYSQL_PWD"),
    "host": getenv("HBNB_MYSQL_HOST"),
    "db": getenv("HBNB_MYSQL_DB"),
    "storage": getenv("HBNB_TYPE_STORAGE"),
    "env": getenv("HBNB_ENV")
}
if config["storage"] == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
