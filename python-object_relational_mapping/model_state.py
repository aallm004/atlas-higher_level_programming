#!/usr/bin/python3
"""Class def of State and instance"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhose/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for item in session.query(State).order_by(State.id):
        print("{}: {}".format(item.id, item.name))

    session.close()

