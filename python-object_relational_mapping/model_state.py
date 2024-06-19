#!/usr/bin/python3
"""defines function that creates base model"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Start of State Class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    id = Column(Integer, primary_key=True, nullable = False, autoincrement=True)
