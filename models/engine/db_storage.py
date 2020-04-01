#!/usr/bin/python3
"""This is the file DBStorage class for AirBnB"""
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class seria
    lizes instances to a JSON file and
    deserializes JSON fi
    le to instances
    Attributes:
        __engine path to the JSON file
        __session: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of base model DBStorage"""
        ENV = os.getenv('HBNB_ENV')
        USER = os.getenv('HBNB_MYSQL_USER')
        PWD = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')

        if ENV != "test":
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                          format(USER, PWD, HOST, DB),
                                          pool_pre_ping=True)
        else:
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query of object depending of the class name
         if cls=none query of all type of objects """
        my_session = self.__session
        if cls:
            if cls.__name__:
                class_to_return = [cls.__name__]
        else:
            class_to_return = [State, City, User]
        dic = {}
        for class_to_print in class_to_return:
            class_list = my_session.query(class_to_print).all()
            for item in class_list:
                key = "{}.{}".format(type(item).__name__, item.id)
                dic.update({key: item})
        return dic

    def new(self, obj):
        """Add new obj
        Args:
            obj: given object
        """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Save to database
        """
        self.__session.commit()

    def reload(self):
        """Create the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            self.__session.delete(obj)
