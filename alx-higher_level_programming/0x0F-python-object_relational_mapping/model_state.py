#!/usr/bin/python3
"""Script that defines a State and an instance."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String

Base = declarative_base()


class State(Base):
    """A state model for creatig state objects for \
    MySQL database.

    id (sqlalchemy.Integer): The state's id in State table.
    name (sqlalchemy.String): The state's name in State table.
    __tablename__ (str): MySQL table name to store States.
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
