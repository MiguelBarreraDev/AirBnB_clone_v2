#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


def get_objects_by_id(CLS, id=None):
    """
    Get records of a specific class that match the id passed
    as argument

    Parameters
    ----------
        CLS: Specific class
        id: Value to indetify objects

    Return
    ------
        store: List of records
    """
    from models import storage
    dict_objects = storage.all(CLS)
    store = list()
    for value in dict_objects.values():
        if value.place_id == id:
            store.append(value)
    return store


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="cities")
    else:
        @property
        def cities(self):
            """Return a list of cities by state"""
            return get_objects_by_id(City, self.id)
