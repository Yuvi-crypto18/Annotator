# db.py

import sqlite3

# Connect once
conn = sqlite3.connect(":memory:", check_same_thread=False)
cursor = conn.cursor()

# Create tables if not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS input (
        presentation_id TEXT,
        name TEXT,
        slide_id TEXT,
        slide_number INTEGER,
        image BLOB
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS output (
        presentation_id TEXT,
        slide_id TEXT,
        tags TEXT
    )
''')

conn.commit()
