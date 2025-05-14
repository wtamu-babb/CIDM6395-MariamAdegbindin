#!/usr/bin/env python3
import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

DB = "flagfootball.db"
CSV_FILES = [
    ("practice_sessions.csv", "PracticeSession", "session_date"),
    ("game_performance.csv",  "GamePerformance",   "game_date"),
    ("injury_log.csv",        "InjuryLog",         "injury_date"),
]

def init_db():
    """Create the three tables if they don't already exist."""
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS PracticeSession (
        id INTEGER PRIMARY KEY,
        session_date TEXT,
        duration_mins INTEGER,
        temperature_f REAL,
        activities TEXT
    )""")
    c.execute("""
    CREATE TABLE IF NOT EXISTS GamePerformance (
        id INTEGER PRIMARY KEY,
        game_date    TEXT,
        touchdowns   INTEGER,
        plays        INTEGER,
        position     TEXT
    )""")
    c.execute("""
    CREATE TABLE IF NOT EXISTS InjuryLog (
        id              INTEGER PRIMARY KEY,
        injury_date     TEXT,
        injury_type     TEXT,
        severity        TEXT,
        recovery_notes  TEXT
    )""")
    conn.commit()
    conn.close()

def preload_data():
    """
    Load CSV data into the database if present.
    Skips any files/columns that aren't found, warns you.
    """
    conn = sqlite3.connect(DB)
    for csv_file, table, date_col in CSV_FILES:
        if not os.path.isfile(csv_file):
            print(f"⚠️  Skipping preload: {csv_file} not found.")
            continue

        df = pd.read_csv(csv_file)
        if date_col not in df.columns:
            print(f"⚠️  Skipping {csv_file}: column '{date_col}' missing.")
            continue

        # Parse the date column into proper datetime strings
        df[date_col] = pd.to_datetime(df[date_col]).dt.strftime("%Y-%m-%d")

        # Build an INSERT statement with the exact columns
        cols        = ", ".join(df.columns)
        placeholders = ", ".join(["?"] * len(df.columns))
        sql         = f"INSERT OR IGNORE INTO {table} ({cols}) VALUES ({placeholders})"

        # Push every row
        conn.executemany(sql, df.values.tolist())
        conn.commit()
        print(f"✅  Preloaded {len(df)} rows into {table} from {csv_file}")
    conn.close()

def add_practice():
    date  = input("Date (YYYY-MM-DD): ")
    duration = int(input("Duration (mins): "))
    temp  = float(input("Temperature (°F): "))
    acts  = input("Activities (comma-sep): ")
    conn  = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO PracticeSession (session_date, duration_mins, temperature_f, activities) VALUES (?,?,?,?)",
        (date, duration, temp, acts)
    )
    conn.commit()
    conn.close()
    print("✓ Practice session logged.\n")

def add_game_performance():
    date = input("Game Date (YYYY-MM-DD): ")
    td   = int(input("Touchdowns: "))
    plays = int(input("Total Plays: "))
    pos  = input("Position: ")
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO GamePerformance (game_date, touchdowns, plays, position) VALUES (?,?,?,?)",
        (date, td, plays, pos)
    )
    conn.commit()
    conn.close()
    print("✓ Game performance logged.\n")

def add_injury():
    date     = input("Injury Date (YYYY-MM-DD): ")
    itype    = input("Injury Type: ")
    severity = input("Severity (mild/moderate/severe): ")
    notes    = input("Recovery Notes: ")
    conn     = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO InjuryLog (injury_date, injury_type, severity, recovery_notes) VALUES (?,?,?,?)",
        (date, itype, severity, notes)
    )
    conn.commit()
    conn.close()
    print("✓ Injury logged.\n")

def view_dashboard():
    conn = sqlite3.connect(DB)
    games = pd.read_sql("SELECT * FROM GamePerformance", conn, parse_dates=["game_date"])
    conn.close()

    # Weekly aggregation
    games["week_end"] = games["game_date"] + pd.to_timedelta((6 - games["game_date"].dt.weekday), unit="d")
    weekly_td   = games.groupby("week_end")["touchdowns"].sum().reset_index()
    weekly_plays = games.groupby("week_end")["plays"].sum().reset_index()

    # Bar chart for touchdowns
    plt.figure(figsize=(8,4))
    plt.bar(weekly_td["week_end"], weekly_td["touchdowns"], color="steelblue")
    plt.title("Weekly Touchdowns")
    plt.xlabel("Week Ending")
    plt.ylabel("Touchdowns")
    plt.tight_layout()
    plt.show()

    # Line chart for plays
    plt.figure(figsize=(8,4))
    plt.plot(weekly_plays["week_end"], weekly_plays["plays"], marker="o", linestyle="-", color="darkorange")
    plt.title("Weekly Total Plays")
    plt.xlabel("Week Ending")
    plt.ylabel("Plays")
    plt.tight_layout()
    plt.show()

def main():
    # 1) ensure schema
    init_db()

    # 2) preload CSVs if you have them
    preload_data()

    # 3) interactive menu
    menu = {
        "1": ("Log Practice Session",    add_practice),
        "2": ("Log Game Performance",    add_game_performance),
        "3": ("Log Injury",              add_injury),
        "4": ("View Dashboard",          view_dashboard),
        "q": ("Quit",                    None)
    }

    while True:
        print("\n--- Flag Football Prototype ---")
        for key,(desc,_) in menu.items():
            print(f"{key}. {desc}")
        choice = input("Choose an option: ").strip().lower()
        if choice == "q":
            print("👋 Goodbye!")
            break
        action = menu.get(choice)
        if action:
            action[1]()
        else:
            print("⚠️  Invalid choice, try again.")

if __name__ == "__main__":
    main()
