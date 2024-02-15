#!/usr/bin/python3
"""Script lists all state objects from hbtn_0e_6_usa db."""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(args[1],
                                                      args[2], args[3])
    engine = create_engine(url=url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).order_by(State.id)
    for state in results:
        print("{}: {}".format(state.id, state.name))
