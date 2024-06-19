#!/usr/bin/python3
"""Fetch and display City objects from the datebase hbtn"""

import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """documentation"""
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>"\
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
