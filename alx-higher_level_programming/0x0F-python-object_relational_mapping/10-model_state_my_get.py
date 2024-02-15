#!/usr/bin/python3
"""Prints the State object with the name passed \
    as arg from hbtn_0e_6_usa db.
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    flag = False
    args = sys.argv
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(args[1],
                                                      args[2], args[3])
    engine = create_engine(url=url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State)
    for state in result:
        if state.name == args[4]:
            flag = True
            print("{}".format(state.id))
            break
    if not flag:
        print("Not found")
