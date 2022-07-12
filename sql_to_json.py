
"""
Langage: Python 3
This function creates a dict from a sqlite3 database
Requirements:
Python3
sqlite3 module
create_connection and query from sqlite3_functions.py
"""


def db_to_dict(db_path: str) -> dict|bool:
    """
This function read all table in a sqlite database, and give back a 
dict

Parameters
----------
db_path : str
    path to / name of the database that needs to be read

Return
------
dict 
    If the database has at least one table, it will return the 
content of the database, in the form:
{
    "table_name1": {
        "1":{...},
        "2":{...},
        ...,
    },
    "table_name2":{
        "1":...
    },
    ...
}
bool
    Returns False, if the database has 0 table

Note
----
This programm needs create_connection and query (see https://github.com/franzele21/cool_code/blob/main/sqlite3_functions.py)
This is perfect, to save/send a sqlite database into a json form
    """
    conn = create_connection(db_path)
    table_exists = query(conn, """SELECT count(name) 
                                    FROM sqlite_master 
                                    WHERE type = 'table';
                                """).fetchall()

    if table_exists[0][0] != 0:
        json_data = {}
        tables_name = query(conn, """SELECT name 
                                        FROM sqlite_master 
                                        WHERE type = 'table' 
                                        AND name != 'sqlite_sequence';
                                    """).fetchall()
        tables_name = [table for list_ in tables_name for table in list_]
        
        for table in tables_name:
            json_data[table] = {}
            columns_name = query(conn, f"SELECT * FROM '{table}';")
            columns_name = [description[0] for description in columns_name.description]
            
            lines  = query(conn, f"SELECT * FROM '{table}';").fetchall()
            for index, item in enumerate(lines):
                data = dict(zip(columns_name, item))
                json_data[table][str(index)] = data

        return json_data
    else:
        return False
