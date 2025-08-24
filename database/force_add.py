import sqlite3
import re

# Input text
data = """
6288897839856	Cathay	3	$	0
6288859785911	Cathay	9	$	0
6288841156324	Cathay	3	$	0
6288834651926	Cathay	3	$	0
6288831974823	Cathay	9	$	0
6288826660005	Cathay	12	$	0
6288809153724	Cathay	3	$	0
6288806282640	Cathay	3	$	0
6288806277118	Cathay	3	$	0
6288799611510	Cathay	9	$	0
6288791094321	Cathay	3	$	0
6288787684347	Cathay	9	$	0
6288783753116	Cathay	9	$	0
6288718835346	Cathay	3	$	0
6288716556823	Cathay	3	$	0
6288288179651	Cathay	3	$	0
6288282225159	Cathay	3	$	0
6288273687758	Cathay	6	$	0
6288259010704	Cathay	3	$	0
6288255695900	Cathay	3	$	0
6288216964420	Cathay	3	$	0
6288209945123	Cathay	9	$	0
6288175918912	Cathay	3	$	0
6288133135303	Cathay	6	$	0
6288127388720	Cathay	3	$	0
6288115915240	Cathay	3	$	0
"""

# Extract numbers (more than 3 digits)
numbers = re.findall(r"\b\d{4,}\b", data)

# Connect to database
conn = sqlite3.connect("database/cathay_database.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

# Ensure table exists
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

# Insert into DB (skip duplicates)
for num in numbers:
    # cursor.execute("SELECT id FROM numbers WHERE number = ?", (num,))
    # if cursor.fetchone() is None:
        cursor.execute("INSERT INTO numbers (number) VALUES (?)", (num,))

# Commit and close
conn.commit()
conn.close()

print(f"Inserted {len(numbers)} numbers (excluding duplicates) into the database.")
