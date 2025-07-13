#!/usr/bin/python3
import mysql.connector
from seed import connect_to_prodev

def stream_users():
    # connect to the database
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)  # ensures each row is returned as a dict

    cursor.execute("SELECT * FROM user_data")  # fetch all rows
    for row in cursor:                         # yield one by one
        yield row

    # cleanup
    cursor.close()
    connection.close()
