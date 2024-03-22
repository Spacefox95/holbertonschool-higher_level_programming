#!/usr/bin/python3
"""
Update a state object in the database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_update = session.query(State).filter_by(
        id=2).order_by(State.id).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
    session.close()
