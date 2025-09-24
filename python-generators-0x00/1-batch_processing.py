#!/usr/bin/python3
"""
1-batch_processing.py
- Implements batch streaming and processing of users from DB
"""

import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """
    Generator: fetch rows in batches from user_data table
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Letho@1arya",          # update if needed
            database="ALX_prodev" # use your database name
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")

        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            yield rows  # yield a whole batch at a time

        cursor.close()
        connection.close()

    except Error as e:
        print(f"Error streaming in batches: {e}")
        return


def batch_processing(batch_size):
    """
    Process each batch -> filter users over age 25
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:  # loop inside the batch
            if int(user["age"]) > 25:
                print(user)
