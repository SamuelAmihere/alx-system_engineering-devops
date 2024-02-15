#!/usr/bin/python3
"""Script that defines a City and an instance."""

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()


class City(Base):
    """A state model for creatig state objects for
    MySQL database.

    id (sqlalchemy.Integer): The city's id in State table.
    name (sqlalchemy.String): The city's name in State table.
    __tablename__ (str): MySQL table name to store cities.
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    __tablename__ = "cities"
