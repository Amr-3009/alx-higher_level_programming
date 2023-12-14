#!/usr/bin/python3
from sqlalchemy import Column, Integar, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = "states"
    id = Column(Integar, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
