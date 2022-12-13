from psycopg2 import connect
from json import load

def open_db_connection():
    with open("./resources/db_info.json") as data:
        db_info = load(data)

    connection = connect(
        host=db_info["HOST"],
        database=db_info["DATABASE"],
        user=db_info["DB_USER"],
        password=db_info["DB_PASS"]
    )

    cursor = connection.cursor()

    return connection, cursor