#!/usr/bin/env python3
import sqlite3
import functools

# decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(query, *args, **kwargs):
        print(f"Executing SQL Query: {query}")
        return func(query, *args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# fetch users while logging the query
if __name__ == "__main__":
    users = fetch_all_users("SELECT * FROM users")
    print(users)
