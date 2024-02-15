#!/usr/bin/python3
"""Adds the State object 'Louisiana' to hbtn_0e_6_usa db.
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

    obj = State(name="Louisiana")
    session.add(obj)
    session.commit()
    print(obj.id)
