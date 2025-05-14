# ss_loader.py

import csv

def load_practice_records(csv_path="practice_sessions.csv"):
    """
    Reads the CSV exported from our Excel mock-up
    and prints each practice record.
    """
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        records = list(reader)
        print(f"Loaded {len(records)} practice records:")
        for r in records[:5]:   # show only first 5 for brevity
            print(
                f" • Player {r['PlayerID']} on {r['Date']}: "
                f"{r['Duration_mins']} mins at {r['Temperature_F']}°F, "
                f"{r['Altitude_ft']} ft"
            )
        if len(records) > 5:
            print(f" … (+{len(records)-5} more)")

if __name__ == "__main__":
    load_practice_records()
