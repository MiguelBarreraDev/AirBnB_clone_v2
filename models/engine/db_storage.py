"""Module that define engine of storage in database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from models import config


classes = [State, City, Place, Review, User, Amenity]


def get_engine():
    """Make link to the MySQL"""
    url = "mysql+mysqldb://{}:{}@{}/{}".format(
        config["user"],
        config["passwd"],
        config["host"],
        config["db"]
    )
    engine = create_engine(url, pool_pre_ping=True)
    return engine


class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Class constructor"""
        self.__engine = get_engine()
        if config["env"] == "test":
            Base.metadata.drop_all(self.__engine)  # Delete all tables

    def all(self, cls=None):
        """Return stored objects in the database"""
        logs = []
        new_dict = {}
        if not cls:
            for classname in classes:
                logs.extend(self.__session.query(classname).all())
        else:
            logs.extend(self.__session.query(cls).all())

        for obj in logs:
            key = obj.__class__.__name__ + "." + obj.id
            new_dict[key] = obj
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
        Base.metadata.create_all(self.__engine)
        config_session = {"bind": self.__engine, "expire_on_commit": False}
        Session = sessionmaker(**config_session)
        self.__session = Session()
