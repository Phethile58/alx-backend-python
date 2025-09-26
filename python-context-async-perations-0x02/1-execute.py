import sqlite3


class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or []
        self.connection = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.cursor.close()
            self.connection.close()


if __name__ == "__main__":
    db_name = "users.db"

    # Ensure table exists and has data
    with ExecuteQuery(db_name, "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"):
        pass
    with ExecuteQuery(db_name, "INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30)):
        pass
    with ExecuteQuery(db_name, "INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25)):
        pass
    with ExecuteQuery(db_name, "INSERT INTO users (name, age) VALUES (?, ?)", ("Charlie", 35)):
        pass

    # Use the context manager to run the given query
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)
    with ExecuteQuery(db_name, query, params) as results:
        for row in results:
            print(row)
