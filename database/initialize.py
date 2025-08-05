import sqlite3

conn = sqlite3.connect("database/temp5.db")
conn.execute("PRAGMA foreign_keys = ON;")  # Enable FK support

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    datetime TEXT NOT NULL,
    cookies TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS email_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email_id INTEGER NOT NULL,
    datetime TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY(email_id) REFERENCES emails(id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS numbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL,
    is_working BOOLEAN NOT NULL DEFAULT 1,
    is_archived BOOLEAN NOT NULL DEFAULT 0,
    last_checked INTEGER NOT NULL DEFAULT 0,
    hits INTEGER NOT NULL DEFAULT 0
)
""")

conn.commit()
conn.close()
