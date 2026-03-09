# 2. Prompt and Context Engineering

## Exercise 1

Ask Claude Code the following questions in **two separate conversations**:

- What does the function `process_data` in utils.py do?
- What does the function `process_data` in @utils.py do?

Questions:

1. How did the tool calls differ between the two conversations?
1. In your own words: what does @ do, and when might you want to use it?

Note: You can ask Claude Code to explain the behavior of Claude Code.

**Goal:** Participants understand (1) how to add files into the context; (2) that the
@-operator allows for deterministic addition of the file content into the context
(though the resulting context might be the same).

## Exercise 2

Continue the session of the previous exercise and work through the following tasks:

**2.1.** Run `/context` and look at the output. What information is shown and why is
this useful to know?

**2.2.** Create a status line for Claude Code that includes at least the context window
and token usage. Are there other things you would include in the status?

**Goal:** (1) Understand how to inspect context usage; (2) Have continuous visibility
into context for the rest of the course; (3) Learn about the `/context` command.

## Exercise 3

Start a new session and work through the following task. Have an eye on your status line
while doing so.

**3.1.** Ask Claude Code to explain the `summarize_csv.py` script to you. Ask at least 2
follow-up questions (for example: How does it handle missing values? Could it support
Excel files?). Run the script on `data.csv`.

**3.2.** You look at the code and think: "This is a lot of manual CSV parsing. Pandas
would solve all of this in five lines." Ask Claude Code to refactor `summarize_csv.py`
to use pandas. Run the script on the sample data and verify the output hasn't changed.
Look at the actual file to confirm the refactoring.

> But then your team lead tells you the code actually needs to run in an environment
> with no external dependencies... time to undo.

**3.3.** Run `/rewind` and select the message where you asked for the refactoring.
Choose "Restore code and conversation". Is the file back to the original? Does Claude
still remember the earlier part of your conversation? What is the difference between
rewinding the conversation and rewinding the code?

**3.4.** It's Friday afternoon and you're a bit annoyed that you can't use the more
elegant pandas version. You close the session (e.g., using Ctrl+D) and call it a day. On
Monday morning, you want to pick up where you left off. Open Claude Code again and
resume the session.

**3.5.** You realize that your context window is filling up, but want to continue
working in the session with a compactified context. Run `/compact` and check how this
affects your context usage.

Note: you can pass focus instructions to compact, e.g. "`/compact` focus on the
pure-Python improvement ideas".

**3.6.** You don't care anymore about the specific messages from Friday and want to free
up context. Run `/clear` and check how this affects your context usage.

**Goal:** Learn how the context-related commands are used and in which situation to use
them.
