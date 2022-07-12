"""
Langage: Python 3

Those functions are used to:
    - create_connection: create a database file (if it doesn't exist) 
and return a <sqlite3.Connection> object to the database
    - query: make a query to a database

Requirements:
Python3
sqlite3 module
"""

import sqlite3
from sqlite3 import Error


def create_connection(path: str, check_same_thread :bool=True) -> sqlite3.Connection:
    """
Establish the connection with the database

Parameters
----------
path : str
    Path to the database
check_same_thread : bool
    activate the check_same_thread of the connection

Returns
-------
sqlite3.Connection or None
    Connection to the database or None
    """
    connection = None
    try:
        connection = sqlite3.connect(path, check_same_thread=check_same_thread)
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def query(connection: sqlite3.Connection, query_: str) -> sqlite3.Cursor:
    """
Makes a query to a database

Parameters
----------
connection : sqlite3.Connection
    Connection to the database on wich the query has to be made
file : str
    FIle which makes the query
query_ : str
    Query to be done on the database

Returns
-------
sqlite3.Cursor or None
    Response (if any) from the database of the query
    """    
    cursor = connection.cursor()
    try:
        cursor.execute(query_)
        connection.commit()
        return cursor
    # the next commentec lines can be enabled for collision handling
    # except sqlite3.OperationalError:
    #     print("Error: the database is locked")
    #     return "locked"
    except Error as e:
        print(f"Error: '{e}'")
        return False
