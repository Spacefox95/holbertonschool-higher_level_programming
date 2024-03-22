#!/usr/bin/python3
"""
Create the class State and an instance
Base = declarative_base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    New class State as database
    New table 'states'
    Args :
    id = INT UNIQUE PRIMARY KEY NOT NULL
    name = STRING(128) NO NULL
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
