#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="cities", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Return a list of cities by state"""
            from models.__init__ import storage
            from models.city import City
            list_cities = list(filter(
                lambda c: c.state_id == self.id,
                storage.all(City).values()
            ))
            return list_cities
