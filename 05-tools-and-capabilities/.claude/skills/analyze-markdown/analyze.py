"""Analyze all markdown files in the project."""

from pathlib import Path

root = Path(__file__).resolve().parents[5]  # navigate up to project root
md_files = sorted(root.rglob("*.md"))

# Filter out hidden dirs and node_modules
md_files = [
    f
    for f in md_files
    if not any(part.startswith(".") or part == "node_modules" for part in f.parts)
]

total_files = len(md_files)
line_counts = []

for f in md_files:
    try:
        lines = f.read_text().splitlines()
        line_counts.append((f.relative_to(root), len(lines)))
    except Exception:
        pass

total_lines = sum(c for _, c in line_counts)
avg_lines = total_lines / total_files if total_files else 0

print(f"Total markdown files: {total_files}")
print(f"Total line count: {total_lines}")
print(f"Average lines per file: {avg_lines:.1f}")
print("\nTop 5 longest files:")
for path, count in sorted(line_counts, key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {count:>5} lines  {path}")
