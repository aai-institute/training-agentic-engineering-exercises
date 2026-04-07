# Exercises: Permissions and Sandboxing

> **⚠️ IMPORTANT: `cd` into `04a-permissions-and-sandboxing/` before starting Claude
> Code.** The exercises depend on project-level settings and data files in this
> directory. To avoid interference from global permission rules, start Claude Code with
> restricted setting sources:

```bash
cd 04a-permissions-and-sandboxing
claude --setting-sources project,local
```

This ignores your global `~/.claude/settings.json` and `~/.claude/settings.local.json`,
so only project-level settings apply.

## Exercise 0: Verification

1. Run `/status`
1. The entry `cwd` should contain
   `training-agentic-engineering-exercises/04a-permissions-and-sandboxing`
1. `Setting sources` should only be `Project local settings`, if you see
   `User settings`, you have to close the session and start a new one with
   ```bash
   claude --setting-sources project,local
   ```

## Exercise 1: The Permission System

This exercise walks you through the core mechanics of Claude Code's permission system.
You'll discover how tool approvals work, how to add rules, and where the system's limits
are.

> **⚠️ Make sure your working directory is `04a-permissions-and-sandboxing/`.**

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
- Open `04a-permissions-and-sandboxing/.claude/settings.local.json` — where is the deny
  rule stored? What does the structure look like?

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
1. Inspect `04a-permissions-and-sandboxing/.claude/settings.local.json` to verify you
   have an **Allow** and **Deny** rule active for `Bash(uv run python *)`.
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

> **⚠️ Make sure your working directory is `04a-permissions-and-sandboxing/`.**

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
