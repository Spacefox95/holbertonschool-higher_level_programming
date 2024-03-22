#!/usr/bin/python3
"""
Create the class City and an instance
Base = declarative_base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


Base = declarative_base()


class City(Base):
    """
    New class State as database
    New table 'states'
    Args :
    id = INT UNIQUE PRIMARY KEY NOT NULL
    name = STRING(128) NO NULL
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
