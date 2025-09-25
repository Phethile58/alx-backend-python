import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

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

    # Create table and insert sample data
    with DatabaseConnection(db_name) as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
        )
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))

    # Use context manager to query data
    with DatabaseConnection(db_name) as cursor:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
