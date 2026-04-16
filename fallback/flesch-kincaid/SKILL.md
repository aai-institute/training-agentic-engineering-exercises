---
name: flesch-kincaid
description: >-
  Compute the Flesch-Kincaid reading-ease score for a single markdown file.
---

# flesch-kincaid

Compute the Flesch reading-ease score for the markdown file the user supplied as the
skill argument. Always use the bundled script — never compute the score inline or with a
different tool.

## Steps

1. Take the raw path argument the user passed to `/flesch-kincaid` (e.g.
   `../03-customization/README.md`). Keep it exactly as typed; do not resolve,
   normalize, or rewrite it.

1. Run the bundled script with that path:

   ```bash
   uv run .claude/skills/flesch-kincaid/score.py <path>
   ```

   The script prints a single line containing the score formatted to two decimals (e.g.
   `59.40`). It exits non-zero with an `Error: ...` message if the argument is missing,
   the file does not exist, or the file does not have a `.md` extension.

1. If the script exits non-zero, surface the error message to the user verbatim and
   stop. Do not emit the success template.

1. On success, respond with **exactly** this single line and nothing else:

   ```
   The Flesch-Kincaid reading-ease score for {path} is {score}.
   ```

   where `{path}` is the literal argument the user typed and `{score}` is the script's
   stdout.
