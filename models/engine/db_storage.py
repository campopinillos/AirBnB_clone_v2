#!/usr/bin/python3
"""This is the file DBStorage class for AirBnB"""

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


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
            class_to_return = [User, State]
        dic = {}
        for class_to_print in class_to_return:
            query = New_session.query(class_to_print)
            class_list = query.all()
            for item in class_list:
                key = "{}.{}".format(type(item).__name__, item.id)
                dic.update({key: item})

        return dic
