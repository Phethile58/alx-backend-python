#!/usr/bin/python3
"""
Run multiple database queries concurrently using asyncio.gather
and aiosqlite for async SQLite operations.
"""

import asyncio
import aiosqlite


async def setup_database():
    """Create and populate the users table for demo purposes."""
    async with aiosqlite.connect(":memory:") as db:
        await db.execute(
            """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )"""
        )
        await db.executemany(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            [
                ("Alice", 30),
                ("Bob", 22),
                ("Charlie", 45),
                ("Diana", 50),
                ("Eve", 28),
            ],
        )
        await db.commit()
    return ":memory:"


async def async_fetch_users(db_name=":memory:"):
    """Fetch all users from the database."""
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()


async def async_fetch_older_users(db_name=":memory:"):
    """Fetch users older than 40 from the database."""
    async with aiosqlite.connect(db_name) as db:
        async with db.execute(
            "SELECT * FROM users WHERE age > 40"
        ) as cursor:
            return await cursor.fetchall()


async def fetch_concurrently():
    """Run both queries concurrently and print results."""
    db_name = await setup_database()

    results_all, results_old = await asyncio.gather(
        async_fetch_users(db_name),
        async_fetch_older_users(db_name),
    )

    print("All users:")
    for row in results_all:
        print(row)

    print("\nUsers older than 40:")
    for row in results_old:
        print(row)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
