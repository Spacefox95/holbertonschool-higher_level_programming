#!/usr/bin/python3
"""
Lists all State objects from
database hbtn_0e_6_usa
"""
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
    current_state = sys.argv[4]
    """
    Create a session
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
        State.name == current_state).order_by(State.id).all()
    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
