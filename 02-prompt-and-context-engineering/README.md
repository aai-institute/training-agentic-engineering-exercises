# Exercises: Prompt and Context Engineering

## Exercise 1: The @ Operator

Ensure you are in the `02-prompt-and-context-engineering/` directory.

Ask Claude Code the following questions in **two separate conversations**:

- What does the function `read_csv` in summarize_csv.py do?
- What does the function `read_csv` in @summarize_csv.py do?

**Questions:**

- How did the tool calls differ between the two conversations?
- In your own words: what does @ do, and when might you want to use it?

## Exercise 2: Context Visibility

Continue one of the sessions of the previous exercise and work through the following
tasks:

### 2.1 Inspect Context Usage

Run `/context` and look at the output.

**Questions:**

- What information is shown and why is this useful to know?
- What are the biggest contributors to your current context usage?

### 2.2 Create a Status Line

Create a status line for Claude Code that includes at least the context window and token
usage. Claude Code helps you with the set-up when you run `/statusline`.

**Questions:**

- How could continuous visibility into context help you during longer sessions?
- Are there other things you would include in the status?

## Exercise 3: Context Management Commands

Continue with the previous session and work through the following tasks. Have an eye on
your status line while doing so.

### 3.1 Explore the Script

Ask Claude Code to explain the `summarize_csv.py` script to you. Ask at least 2
follow-up questions. Examples:

- How does it handle missing values?
- Could it support Excel files?

Run the script on `data.csv`.

> **Note:** You can toggle detailed outputs using `ctrl+o`.

### 3.2 Refactor to Pandas

Run `/context` and write down how much free space is left.

You look at the code and think: *"This is a lot of manual CSV parsing. Pandas would
solve all of this in five lines."*

Ask Claude Code to refactor `summarize_csv.py` to use pandas. Run the script on the
sample data and verify the output hasn't changed. Look at the Python file to confirm the
refactoring.

Run `/context` again and write down how much free space is left after the refactoring.

### 3.3 Rewind

But then your team lead tells you the code actually needs to run in an environment with
no external dependencies... time to undo.

Run `/rewind` and select the message where you asked for the refactoring. Choose
"Restore code and conversation".

**Questions:**

- Is the file back to the original?
- Is your free space back to before the refactoring (validate using `/context`)?
- What is the difference between rewinding the conversation and rewinding the code?
- When would you use `/rewind` vs `git checkout`?

### 3.4 Rename and Resume

It's Friday afternoon and you're a bit annoyed that you can't use the more elegant
pandas version.

1. To find the session again in the future you rename it to "Summarize CSV" using the
   `/rename` command.
1. You then close the session (e.g., using Ctrl+D) and call it a day.
1. You now want to pick up where you left off. Open Claude Code again and resume the
   session.

**Questions:**

- When would you want to resume an old session?

### 3.5 Compact

You realize that your context window is filling up, but want to continue working in the
session with a compactified context. Run `/compact` and check how this affects your
context usage.

> **Note:** you can pass focus instructions to compact, e.g. "`/compact` focus on the
> performance improvement ideas".

**Questions:**

- How did your context usage change?
- In your own words: What does compact do?
- What would you do if you want to compactify a conversation but you want more control
  over the process?
- Could you use compactification for stopping and effictively resuming sessions?

### 3.6 Clear

You don't care anymore about the specific messages from Friday and want to free up
context completely. Run `/clear` and check how this affects your context usage.

**Questions:**

- When would you use `/clear` instead of `/compact`?

### 3.7 To clear or not to clear

Discuss:

If your conversation drifts into a wrong direction. Do you try to "save" the
conversation/context or do you clear quickly?
