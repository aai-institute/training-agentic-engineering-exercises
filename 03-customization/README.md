# Exercises: Customization

## Exercise 1: Experience CLAUDE.md

1. Create the folder `.claude` in the exercise directory and populate it with
   `.claude/CLAUDE.md` containing a single instruction: "Docstrings must contain ONLY
   emoji's."
1. Start a new session. Ask Claude Code to write a `hello` function in a new `hello.py`
   file that prints "Hello World!".
1. Look at the generated code. Did Claude follow the instruction?
1. Run `/context`. Can you find where the CLAUDE.md instruction appears in the context?

**Reflections:**

- How many tokens does this one-line instruction cost per conversation?
- What would happen if you tell Claude to never use emojis in code in another
  instruction file?

## Exercise 2: Notification Hook

Create a hook that notifies you when Claude Code needs your input or has finished a
task:

1. Ask Claude Code: *"I want a notification hook that alerts me whenever you need my
   input or finish a task. Create it in `.claude/settings.local.json`. Figure out what
   works on my OS."*
1. Let Claude Code detect your operating system and choose the right notification
   approach. Review the generated hook in `.claude/settings.local.json`.
1. Identify the **when** (event), **which** (matcher), and **what** (handler) from the
   slides.
1. Run `/hooks` to confirm the hook is active.
1. Give Claude Code a small task (e.g., update the `hello` function in `hello.py` to
   print "Hello Claude"), switch to a different window, and watch for the notification.

> **Note (macOS):** Focus modes (Work, Do Not Disturb) suppress notifications. If the
> hook seems broken, check your Focus mode first.

**Reflections:**

- What are the security implications of cloning a repo that has hooks pre-configured?

> **Reference:**
> [Hooks guide — Get notified when Claude needs input](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)

## Bonus: Set Up a Status Line

> Skip this if you already have a status line configured.

Set up a status line so you always see your context usage. The `/statusline` command
accepts a natural language description of what you want and guides you through the
process. For example:

```
/statusline show context percentage
```

**Reflections:**

- How could continuous visibility into context help you during longer sessions?
- Are there other things you would include in the status line?

> **Reference:** [Status line documentation](https://code.claude.com/docs/en/statusline)
