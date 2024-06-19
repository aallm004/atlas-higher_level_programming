#!/usr/bin/python3
"""Lists all states from database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql://{username}:{password}@localhose:3306/{database}")
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()
    
    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))

    session.close()
