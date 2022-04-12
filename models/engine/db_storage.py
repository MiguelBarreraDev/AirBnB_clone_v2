"""Module that define engine of storage in database"""
from sqlalchemy import create_engine, engine
from sqlalchemy.orm.scoping import scoped_session
from base_model import Base


def connect(**kwrgs):
    """Make link to the MySQL"""
    from models.__init__ import config
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
        from models.__init__ import config
        self.__engine = connect()
        if config["env"] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        pass

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
        from sqlalchemy.orm import sessionmaker
        Base.metadata.create_all(self.__engine)
        config_session = {
            "bind": self.__engine,
            "expire_on_commit": False,
            "scoped_session": "thread-safe"
        }
        Session = sessionmaker(**config_session)
        self.__session = Session()
