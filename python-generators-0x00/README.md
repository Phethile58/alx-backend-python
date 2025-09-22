# Python Generators Project - 0x00

This project sets up a MySQL database, creates a table, and populates it with sample user data from a CSV file.

## Files
- **0-main.py** → Driver script to test the functions in `seed.py`.
- **seed.py** → Handles database setup and seeding.
- **user_data.csv** → Sample data for populating the database.
- **README.md** → Project documentation.

## Database Schema
Database: `ALX_prodev`  
Table: `user_data`

| Field   | Type       | Constraints                   |
|---------|-----------|--------------------------------|
| user_id | VARCHAR(36) | Primary Key, UUID, Indexed    |
| name    | VARCHAR(255) | NOT NULL                     |
| email   | VARCHAR(255) | NOT NULL                     |
| age     | DECIMAL     | NOT NULL                     |

## Usage
1. Make sure you have **MySQL server** and the **mysql-connector-python** library installed:
   ```bash
   sudo apt update
   sudo apt install mysql-server
   pip install mysql-connector-python
