#!/usr/bin/python3
"""Lists all City objects from from hbtn_0e_6_usa db.
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

    result = session.query(City).order_by(City.id)
    for city in result:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
