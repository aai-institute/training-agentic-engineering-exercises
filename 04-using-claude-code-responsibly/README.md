# 4. Using Claude Code Responsibly

**Topics, Questions and Takeaways:**

**Learning Goals:**

**Exercises:**

For the following exercises, we kindly ask that you temporarily disable global Claude
settings.

macOS / Linux / WSL:

```bash
mv ~/.claude/settings.json ~/.claude/settings.json.bak
mv ~/.claude/settings.local.json ~/.claude/settings.local.json.bak
```

To restore afterwards:

```bash
mv ~/.claude/settings.json.bak ~/.claude/settings.json
mv ~/.claude/settings.local.json.bak ~/.claude/settings.local.json
```

## Exercise 1

Start a new session and work through the following task.

1. Ask Claude how to prevent reading from the data subdirectory.
1. Call `/permissions`, cycle to the tab deny and add `Read(data/**)` (choose Project
   Settings (local)).
1. `/clear` the session, ask Claude Code to read the file `./data/some_data.txt`. Is the
   deny rule working?
1. Open the file `.claude/settings.local.json`, you should see a "deny" block containing
   the Read rule you added.

**Goal:** Understand the permission rules and modes and how they work together.

## Exercise 2

How do I ensure that data doesn't leak?

1. When Deny is not enough, create an example to create code to read from a Denied read
   folder.
1. Build mock data (do not inject your data into claude code to build mock data!!!)
   - Manually create one datapoint and use claude code to extrapolate.
   - Extract schema from your data (only meta information, you could also use a local
     LLM for this or simple code), use Claude code to extrapolate the schema.

## Exercise 3

Idea: We give them a simple prompt that is "malicious" and leads to CC creating a script
and running with the result of a pop up that says "You have been hacked!". Then they
have to use the practices seen in the chapter to avoid it.

- `--dangerously-skip-permissions` showcase, inject a prompt to read MAC, create a pop
  up to alarm.

**Goal:** Participants learn that (1) blindly accepting CC commands can be dangerous;
and (2) using `--dangerously-skip-permissions` is (obviously) dangerous.

## Exercise 4 (optional)

Run Claude Code in docker or Sandboxing feature of Claude Code.

## Exercise 5

Quiz (Practical / real-life situations: What are the mitigation strategies /
implications?)
