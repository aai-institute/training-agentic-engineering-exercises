---
name: analyze-markdown
description: >
  Analyze the project's markdown documentation. Use this skill when the user asks
  about documentation coverage, file counts, line statistics, or which markdown
  files are the longest.
---

Run the bundled analysis script to report markdown file statistics. Always use the exact
script at `.claude/skills/analyze-markdown/analyze.py` — do not write a new one.

```bash
python .claude/skills/analyze-markdown/analyze.py
```
