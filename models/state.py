#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


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
            from models import storage
            dict_objects = storage.all(City)
            store = list()
            for value in dict_objects.values():
                if value.state_id == self.id:
                    store.append(value)
            return store
