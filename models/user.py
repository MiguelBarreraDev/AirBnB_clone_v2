#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String
from os import getenv
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """
    Model of the User table in the database
    """
    __tablename__ = "users"
    if getenv('HBNB_TYPE_STORAGE') == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user')
        reviews = relationship('Review', backref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
