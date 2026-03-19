"""Summarize a CSV file with per-department statistics."""

import sys
from pathlib import Path


def read_csv(filepath):
    """Read a CSV file and return headers and a list of row dictionaries.

    Parses the file manually by splitting each line on commas.
    """
    path = Path(filepath)
    text = path.read_text()
    lines = [line.strip() for line in text.strip().splitlines()]

    headers = lines[0].split(",")
    rows = []
    for line in lines[1:]:
        if not line:
            continue
        values = line.split(",")
        row = {}
        for i, header in enumerate(headers):
            row[header] = values[i].strip() if i < len(values) else ""
        rows.append(row)
    return headers, rows


def compute_statistics(rows):
    """Compute per-department statistics: headcount, total hours, total cost.

    Rows with missing hours or hourly_rate are skipped with a warning.
    """
    departments = {}

    for row in rows:
        dept = row.get("department", "Unknown")
        hours_str = row.get("hours", "")
        rate_str = row.get("hourly_rate", "")

        if not hours_str or not rate_str:
            name = row.get("name", "?")
            date = row.get("date", "?")
            print(f"  Warning: skipping incomplete row ({name}, {date})")
            continue

        hours = float(hours_str)
        rate = float(rate_str)

        if dept not in departments:
            departments[dept] = {
                "entries": 0,
                "total_hours": 0.0,
                "total_cost": 0.0,
                "rates": [],
            }

        stats = departments[dept]
        stats["entries"] += 1
        stats["total_hours"] += hours
        stats["total_cost"] += hours * rate
        stats["rates"].append(rate)

    return departments


def format_report(stats):
    """Print a formatted summary report to stdout."""
    print("=" * 50)
    print("Department Summary")
    print("=" * 50)

    overall_hours = 0.0
    overall_cost = 0.0

    for dept, data in sorted(stats.items()):
        avg_rate = sum(data["rates"]) / len(data["rates"])
        print(f"\n{dept}")
        print(f"  Entries:      {data['entries']}")
        print(f"  Total hours:  {data['total_hours']:.1f}")
        print(f"  Total cost:   ${data['total_cost']:.2f}")
        print(f"  Avg rate:     ${avg_rate:.2f}/hr")

        overall_hours += data["total_hours"]
        overall_cost += data["total_cost"]

    print("\n" + "-" * 50)
    print(f"Overall: {overall_hours:.1f} hours, ${overall_cost:.2f} total cost")
    print("=" * 50)


def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = Path(__file__).parent / "data.csv"

    print(f"Reading {filepath} ...\n")
    headers, rows = read_csv(filepath)
    stats = compute_statistics(rows)
    format_report(stats)


if __name__ == "__main__":
    main()
