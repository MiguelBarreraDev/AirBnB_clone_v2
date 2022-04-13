#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', ForeignKey('places.id'), nullable=False),
    Column('amenity_id', ForeignKey('amenities.id'), nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
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
        amenity_ids = []
        reviews = relationship(
            'Review', backref='place', cascade='delete'
        )
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False,
            back_populates="place_amenities"
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

        @property
        def reviews(self):
            """Return the list of the reviews of a place"""
            from models.review import Review
            from models.__init__ import storage
            return [filter(
                lambda rw: rw.place_id == self.id,
                storage.all(Review).values()
            )]

        @property
        def amenities(self):
            """ returns the list of Review instances with place_id equals
            to the current Amenity.id """
            from models.amenity import Amenity
            from models.__init__ import storage
            dict_amenity = storage.all(Amenity)
            store = list()
            for key, value in dict_amenity.items():
                if value.place_id == self.id:
                    store.append(value)
            return store
