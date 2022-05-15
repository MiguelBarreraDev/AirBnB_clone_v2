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


# List of all models in the database
classes = [State, City, Place, Review, User, Amenity]


def get_engine():
    """
    Function definition that configure a sqlalchemy engine

    Return
    ------
        engine: Link to database
    """
    url = "mysql+mysqldb://{}:{}@{}/{}".format(
        config["user"],
        config["passwd"],
        config["host"],
        config["db"]
    )
    engine = create_engine(url, pool_pre_ping=True)
    return engine


class DBStorage:
    """
    Define instances to interact with the database. Abstracting the
    sql languaje.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Class constructor to initialize properties on the proect
        """
        self.__engine = get_engine()
        if config["env"] == "test":
            Base.metadata.drop_all(self.__engine)  # Delete all tables

    def all(self, cls=None):
        """
        Return all objects stored in the database or some objects
        of a specifi class

        Parameters
        ----------
            cls: Specific class to return objects

        Return
        ------
            new_dict: Dictionary of objects
        """
        logs = []
        new_dict = {}
        # Get objects from the database
        if not cls:
            for classname in classes:
                logs.extend(self.__session.query(classname).all())
        else:
            logs.extend(self.__session.query(cls).all())
        # Duilding the dictionary
        for obj in logs:
            key = obj.__class__.__name__ + "." + obj.id
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """
        Add the object to the current database session

        Paramaeters
        -----------
            obj: Object to store
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None

        Parameters
        ----------
            obj: Object to delete
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and define the current session
        """
        # Create all tables in the database
        Base.metadata.create_all(self.__engine)
        # Set up a session
        config_session = {"bind": self.__engine, "expire_on_commit": False}
        Session = sessionmaker(**config_session)
        self.__session = Session()
