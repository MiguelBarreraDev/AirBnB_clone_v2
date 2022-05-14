#!/usr/bin/python3
"""Module that define engine of storage in database"""
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity


def connect(**kwrgs):
    """Make link to the MySQL"""
    import models
    config = models.config
    url = "mysql+mysqldb://{}:{}@{}/{}".format(
        config["user"], config["passwd"], config["host"], config["db"]
    )
    engine = create_engine(url, pool_pre_ping=True)
    return engine


class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Class constructor"""
        import models
        config = models.config
        self.__engine = connect()
        if config["env"] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_list = []
        new_dict = {}
        if not cls:
            list_class = [State, City, Place, Review, User, Amenity]
            for my_class in list_class:
                obj_list.extend(self.__session.query(my_class).all())
        else:
            obj_list.extend(self.__session.query(cls).all())

        for obj in obj_list:
            new_dict[type(obj).__name__ + "." + obj.id] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and the current session"""
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        config_session = {
            "bind": self.__engine,
            "expire_on_commit": False,
        }
        Session = sessionmaker(**config_session)
        self.__session = scoped_session(Session)

    def close(self):
        """Remove Session"""
        self.__session.remove()
