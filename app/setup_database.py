
# DB Schema
import sqlite3

def connect_db():
    # Create and return the database connection
    conn = conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn



