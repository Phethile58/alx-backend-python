#!/usr/bin/python3
"""
seed.py - Setup MySQL database ALX_prodev, create table user_data,
and populate it with CSV data.
"""

import mysql.connector
from mysql.connector import Error
import csv
import uuid


def connect_db():
    """
    Connects to the MySQL server (without selecting a specific DB).
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # update if needed
            password="Letho@1arya"        # update if needed
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def create_database(connection):
    """
    Creates the ALX_prodev database if it does not exist.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """
    Connects directly to the ALX_prodev database.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",   # update if needed
            password="Letho@1arya",   # update if needed
            database="ALX_prodev"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None


def create_table(connection):
    """
    Creates the user_data table if it does not exist.
    """
    try:
        cursor = connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        );
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_file):
    """
    Inserts data from CSV into user_data table if not already present.
    CSV expected format: name,email,age
    """
    try:
        cursor = connection.cursor()
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # check if record already exists by email
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (row['email'],))
                if not cursor.fetchone():
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (str(uuid.uuid4()), row['name'], row['email'], row['age'])
                    )
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting data: {e}")
    except FileNotFoundError:
        print(f"CSV file {csv_file} not found")
if __name__ == "__main__":
    # Step 1: connect without selecting a DB
    connection = connect_db()
    if connection:
        create_database(connection)
        connection.close()
        print("Database checked/created ✅")

        # Step 2: connect to ALX_prodev
        connection = connect_to_prodev()
        if connection:
            create_table(connection)
            print("Table checked/created ✅")

            # Step 3: insert data from CSV
            insert_data(connection, "user_data.csv")
            print("Data inserted ✅")

            connection.close()

