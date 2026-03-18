# 4. Using Claude Code Responsibly

**Exercises:**

**Before you start:** To avoid interference from global permission rules, start Claude
Code with restricted setting sources for these exercises:

```bash
claude --setting-sources project,local
```

This ignores your global `~/.claude/settings.json` and `~/.claude/settings.local.json`,
so only project-level settings apply.

## Exercise 1: The Permission System

This exercise walks you through the core mechanics of Claude Code's permission system.
You'll discover how tool approvals work, how to add rules, and where the system's limits
are.

**Setup:** Step to the subdirectory `exercises/04-using-claude-code-responsibly/`, open
a terminal in the directory and start a fresh Claude Code session.

### 1.1 Observe Default Permission Behavior

Try these three operations in your session, one at a time:

1. Ask Claude Code to read `./data/sales_report.csv` and summarize its contents.
1. Ask Claude Code to create a file `hello.py` that prints "Hello".
1. Ask Claude Code to run `uv run python hello.py`.

**Questions:**

- Which of the three operations required your explicit approval?
- Claude Code groups tools into three categories with different approval behavior. Can
  you map each operation above to a category?

| Tool type         | Example          | Approval required? |
| :---------------- | :--------------- | :----------------- |
| Read-only         | Read, Grep, Glob | ?                  |
| File modification | Edit, Write      | ?                  |
| Bash commands     | Shell execution  | ?                  |

### 1.2 Adding Deny Rules

1. Run `/permissions` in your session. You'll see the permission management UI with
   Allow and Deny sections.
1. Add a **Deny** rule: `Read(data/**)` — when prompted for a settings file, choose
   **Project Settings (local)**.
1. Exit the dialog with `Esc`
1. Ask Claude Code to read `./data/sales_report.csv` and summarize its contents again.

**Questions:**

- What happened when Claude tried to read the denied path?
- Open `exercises/04-using-claude-code-responsibly/.claude/settings.local.json` — where
  is the deny rule stored? What does the structure look like?

### 1.3 Allow Rules and Wildcards

1. Via `/permissions`, add an **Allow** rule: `Bash(uv run python *)` (choose Project
   Settings (local)).
1. Exit the dialog with `Esc`
1. Ask Claude Code to run `uv run python hello.py`.

**Questions:**

- Did Claude ask for permission this time?
- Does the rule `Bash(uv run python *)` also match `uv run hello.py` (short uv syntax to
  call a python script)? If not, how would you fix it?

### 1.4 Rule Precedence

1. Via `/permissions`, add a **Deny** rule: `Bash(uv run python *)` (choose Project
   Settings (local)).
1. Inspect `exercises/04-using-claude-code-responsibly/.claude/settings.local.json` to
   verify you have an **Allow** and **Deny** rule active for `Bash(uv run python *)`.
1. Start a new session with `/clear`.
1. Ask Claude Code to run `uv run python hello.py`.

**Questions:**

- What happened? You now have both an Allow *and* a Deny rule for the same pattern.
- What does Claude answer, if you ask about the precedence of permission rules?

### 1.5 Permission Modes

Claude Code supports several permission modes that change the overall approval behavior.
You can cycle through them via `shift+tab`.

1. Press `shift+tab` until you see `accept edits on`
1. Ask Claude to modify `hello.py` to print "Hello World" instead of just "Hello".
1. Ask Claude to rename the file to `hello_world.py`.
1. Now press `shift+tab` until you see `plan mode on`
1. Ask Claude to modify `hello_world.py` to print "Hello Claude!"

**Questions:**

- What changed in comparison to the default mode?
- What does Claude answer, if you ask when and why to use `Plan` or `Accept Edits` mode?

## Exercise 2: Working with Sensitive Data

When you work with genuinely sensitive data (personal records, credentials, proprietary
datasets), you need strategies beyond permissions.

### 2.1 The Limits of Deny Rules

1. Run `/permissions` and switch to `Allow` tab. Make sure you see `Bash(uv run *.py)`.
1. Switch to `Deny` tab and make sure you see `Read(data/*)`.
1. Exit the `/permissions` menu (with `ESC`).
1. Now ask Claude Code to run `uv run read_csv.py` and show you the result in a table
   format.

**Questions:**

- Did you see the data?
- If yes, why did this happen despite the **Deny** rule to read the data?
- What does this imply for working with genuinely sensitive data?
- Ask Claude how to prevent sensitive data from being stored in context.

### 2.2 Sandbox

1. Enter the sandbox dialog with `/sandbox` and select
   `Sandbox BashTool, with regular permissions`
1. If the sandbox dialog closed, enter it again. Verify that on the tab `Config` you see
   `Filesystem Read Restrictions: Denied: data`
1. Ask Claude to `uv run read_csv.py`.
1. Prompt Claude in the following way "Run `uv run read_csv.py` without sandbox."
1. Enter the sandbox dialog again, switch to the tab `Overrides` and choose
   `Strict sandbox mode`.
1. Again, prompt Claude in the following way "Run `uv run read_csv.py` without sandbox."

**Questions:**

- In default and in sandbox mode you have a **Deny** rule now. What is the difference?
- What changes when you run in `Strict sandbox mode` compared to
  `Allow unsandboxed fallback`?
- Do you see any downsides of the `Strict sandbox mode`?

### 2.3 (Bonus/Optional) Docker Sandbox

Requires:

- Docker Desktop 4.58 or later

Be aware, this will take some setup time, due to downloading additional docker layers.
The exercise is completely optional, feel free to skip it.

1. Open a new terminal or close the running Claude session. Make sure your current
   working directory is `exercises/04-using-claude-code-responsibly`.
1. Depending on which billing model you use (API-billing vs. subscription), do the
   following:
   - For API-billing, set the environment variable `ANTHROPIC_API_KEY` with your key and
     run `ANTHROPIC_API_KEY=sk-ant-api03-xxxxx docker sandbox run claude`
   - For subscription, run `docker sandbox run claude` and within the session run
     `/login` (see also
     [login in the sandbox](https://docs.docker.com/ai/sandboxes/get-started/#run-your-first-sandbox)).
1. Follow the dialog for setting appearance configuration.
1. Ask Claude to give you a summary of `../03-customization/README.md`

**Questions:**

- Did you get a summary? If not what kind of message did claude give you?
- How does the docker sandbox differ from the claude built-in sandbox?
