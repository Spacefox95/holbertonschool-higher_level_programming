#!/usr/bin/python3
"""
Print all City objects from the database hbtn_0e_14_usa
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    """
    Connecting to MySQL server
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    """
    Create a session
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(
        State, City.state_id == State.id).order_by(City.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
