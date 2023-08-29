#!/usr/bin/python3
""" A module to define the state table using SQLAlchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(doc="A base class for mapping tables using SQLAlchemy")


class State(Base):
    """A class that maps to the states table"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(id={}, name={})>".format(self.id, self.name)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)
