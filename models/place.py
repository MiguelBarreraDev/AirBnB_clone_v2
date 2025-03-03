#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id', String(60),
            ForeignKey('places.id'), nullable=False
        ),
        Column(
            'amenity_id', String(60),
            ForeignKey('amenities.id'), nullable=False
        )
    )


class Place(BaseModel, Base):
    """
    Model of the Place table in the database
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place')
        amenities = relationship(
            "Amenity", secondary="place_amenity",
            viewonly=False, back_populates="place_amenities"
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """
            Return all reviews instances associated with a place
            """
            from models import storage
            dict_objects = storage.all(Review)
            store = list()
            for value in dict_objects.values():
                if value.place_id == self.id:
                    store.append(value)
            return store

        @property
        def amenities(self):
            """
            Return the list of amenity instances associated with a place
            """
            from models import storage
            dict_objects = storage.all(Amenity)
            store = list()
            for value in dict_objects.values():
                if value.place_id == self.id:
                    store.append(value)
            return store
