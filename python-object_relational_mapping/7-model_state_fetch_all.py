#!/usr/bin/python3
"""Lists all states from database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

def list_states(username, password, db_name):

    out = "mysql://{}:{}@localhose:3306/{}"
    engine = create_engine(out.format(username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    Session.close()
