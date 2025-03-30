
# DB Schema
import sqlite3


def connect_db():
    # Create and return the database connection
    db = 'app/library.db'
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn



