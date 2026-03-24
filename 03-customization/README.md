# 3. Customization

## Exercise 1

Start a new session.

1. Ask Claude Code to implement a function that calculates the mean and standard
   deviation of a list of numbers in a new `stats_utils.py` file. Look at the
   implementation and note the variable names, docstring style, and conventions Claude
   Code chose.

1. Now create the folder `.claude` in the project root and populate it with
   `.claude/CLAUDE.md` containing a single line: "Always write Google-style docstrings
   with an explicit 'Examples' section that contains a runnable doctest."

1. Start a **new session** and give the exact same prompt as in (1) except to write to
   `stats_utils2.py`. Compare the outputs.

Questions:

1. What changed between the two outputs?
1. Run `/context`. Can you see where the CLAUDE.md instruction appears?
1. How many tokens does this one-line instruction cost per conversation?

**Goal:** (1) Experience that instructions influence the output; (2) Understand that
instructions consume context every session.

## Exercise 2

Instruction A in `.claude/CLAUDE.md` (project level) and Instruction (not A) in
`~/.claude/CLAUDE.md` (user-level). Possible examples: **think of a better example!! Use
an example that they definitely do not want to integrate into their CLAUDE.md (e.g.,
smth like emojis in ChatGPT).**

## Exercise 3

Build a proper `.claude/CLAUDE.md` for your project and apply best practices (as taught
in slides). `/init`. Commit it?

## Exercise 4: Create a Status Line

> **Note:** If you already have a status line configured, skip this exercise.

Set up a status line so you always see your context usage. The `/statusline` command
accepts a natural language description of what you want. For example:

```
/statusline show context percentage
```

**Questions:**

- How could continuous visibility into context help you during longer sessions?
- Are there other things you would include in the status?
