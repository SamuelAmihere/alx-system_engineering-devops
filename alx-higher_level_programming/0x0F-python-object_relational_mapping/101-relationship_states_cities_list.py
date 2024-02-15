#!/usr/bin/python3
"""lists all State objects from hbtn_0e_6_usa db.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
    args = sys.argv
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(args[1],
                                                      args[2], args[3])
    engine = create_engine(url=url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id)
    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
