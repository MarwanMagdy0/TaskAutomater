import sqlite3
import json
from pathlib import Path
from datetime import datetime

DB_PATH = "database/database.db"
EMAILS_JSON_PATH = "emails.json"
COOKIES_BASE_DIR = Path(".")

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = ON;")
cur = conn.cursor()

# Load the JSON mapping
with open(EMAILS_JSON_PATH, "r") as f:
    emails_data = json.load(f)

for path_str, logs in emails_data.items():
    print(f"Processing path: {path_str}")
    json_path = COOKIES_BASE_DIR / path_str
    if not json_path.exists():
        print(f"[!] Skipping missing file: {json_path}")
        continue

    # Extract email from filename
    email = json_path.stem  # e.g., 'kv1xczpgxf'
    
    # Extract date from folder name (e.g., '23_7')
    try:
        folder_date = json_path.parent.name  # 'tradingview_cookies_23_7'
        date_part = folder_date.split("_")[-2:]  # ['23', '7']
        print(f"Extracted date part: {date_part}")
        base_date = datetime(day=int(date_part[0]), month=int(date_part[1]), year=2025)
    except Exception as e:
        print(f"[!] Failed to extract date from {path_str}: {e}")
        continue

    # Load cookies JSON string
    with open(json_path, "r") as f:
        cookies_json = f.read()

    # Use the first log as the main datetime for the email row
    main_datetime_str = base_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Normalize date format
    try:
        dt_obj = datetime.strptime(main_datetime_str, "%Y-%m-%d %I:%M:%S %p")
        main_datetime = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(f"[!] Failed to parse datetime: {main_datetime_str}: {e}")
        main_datetime = base_date.strftime("%Y-%m-%d %H:%M:%S")

    # Insert into emails table
    cur.execute("INSERT INTO emails (email, datetime, cookies) VALUES (?, ?, ?)", 
                (email, main_datetime, cookies_json))
    email_id = cur.lastrowid

    # Insert logs
    for log_time in logs:
        try:
            dt_obj = datetime.strptime(log_time, "%Y-%m-%d %I:%M:%S %p")
            dt_str = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
        except:
            dt_str = log_time  # fallback if already in 24h format
        cur.execute("INSERT INTO email_logs (email_id, datetime, status) VALUES (?, ?, ?)",
                    (email_id, dt_str, "CODE_SENT"))

conn.commit()
conn.close()
print("✅ Import complete.")
