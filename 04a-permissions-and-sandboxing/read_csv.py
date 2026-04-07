import csv
from pathlib import Path

data_dir = Path(__file__).parent / "data"

if not data_dir.exists():
    print(f"Directory '{data_dir}' does not exist.")
    raise SystemExit(1)

csv_files = sorted(data_dir.glob("*.csv"))

if not csv_files:
    print("No CSV files found in data/")
    raise SystemExit(0)

for csv_file in csv_files:
    print(f"=== {csv_file.name} ===")
    with open(csv_file, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(", ".join(row))
    print()
