"""
This program saves the info of the json file into a PostgreSQL database.
"""

import json
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


try:
    engine = create_engine(os.getenv("DATABASE_URL"))
except AttributeError as e:
    # print(e, type(e))
    print("Attribute Error! Please set the environment variable 'DATABASE_URL' to a PostgreSQL URL.")
    print("Program exiting...")
    sys.exit(1)  # exit the program 'abnormally', the program would continue without this statement
except Exception as e:
    print(e, type(e))
    print("Program exiting...")
    sys.exit(1)  # exit the program 'abnormally'
else:  # the else block will only execute if no errors were raised
    db = scoped_session(sessionmaker(bind=engine))


print("Hello World")
