"""Module that define engine of storage in database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_model import Base


def connect(**kwrgs):
    """Make link to the MySQL"""
    from models.__init__ import config   
    url = "mysql+mysqldb://{}:{}@{}/{}".format(
        config["user"], config["passwd"], config["host"], config["db"]
    )
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return {"engine": engine, "session": session}


class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Class constructor"""
        from models.__init__ import config   
        self.__engine = connect()["engine"]
        self.__session = connect()["session"]
        if config["env"] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query for All objects depending of the class name"""
        if not cls:
