#!/usr/bin/python3
"""
0-stream_users.py - Stream rows from user_data table one by one using a generator
"""

import mysql.connector
from mysql.connector import Error


def stream_users():
    """
    Generator that yields rows from user_data table one by one as dictionaries.
    """
    try:
        # connect to ALX_prodev
        connection = mysql.connector.connect(
            host="localhost",
            user="root",   # change if needed
            password="Letho@1arya",   # change if needed
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        # one loop only
        for row in cursor:
            yield row

        cursor.close()
        connection.close()

    except Error as e:
        print(f"Error streaming users: {e}")
        return
