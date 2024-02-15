#!/usr/bin/python3
"""Lists all City objects from hbtn_0e_6_usa db.
"""

import sys
from model_state import State
from model_city import City
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

    result = session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id)
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
