#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="cities", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Return a list of cities by state"""
            from models.__init__ import storage
            from models.city import City
            list_cities = [filter(
                lambda c: c.state_id == self.id,
                storage.all(City).values()
            )]
            return list_cities
