#!/usr/bin/python3
"""
SQLAlchemy Model Definition for States

This module defines a SQLAlchemy model for the "states" table.

Usage:
    1. Define the State class to represent the "states" table.
    2. Use the class in conjunction with SQLAlchemy to interact with the
       database.

Dependencies:
    - SQLAlchemy: This module requires the SQLAlchemy library. You can install
      it using:
          pip install sqlalchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State Class

    Represents a row in the "states" table.

    Attributes:
        id (int): Primary key for the state.
        name (str): Name of the state (maximum length: 128 characters).
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
