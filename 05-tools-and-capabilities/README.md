# 5. Tools and Capabilities

**Description:** This section surveys the main ways Claude Code can act and be extended:
built-in tools, external integrations via the Model Context Protocol (MCP), reusable
"skills" (codified instructions/patterns), subagents (role/task decomposition), and
hooks (lightweight automation around events). The focus is on what each mechanism is
for, how they differ, and what tradeoffs they introduce.

**Topics, Questions and Takeaways:**

`(Keywords: Built-in tools, CLI tools via Bash, Skills, MCPs, Subagents, Hooks, Plug-ins)`

______________________________________________________________________

## Skills

### Exercise 1

TODO: What about switching to a more complex example, create a bar chart of word counts
per file or calculate the
[Flesch-Kincaid reading score](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests)
for each chapter's README. Will trigger a python execution more consistently.

1. Prompt claude code to calculate the Flesch-Kincaid reading score for each chapter's
   README.
1. Observe the tool calling details (ctrl+o).
1. After success, /clear the context and run the same prompt again.

Questions:

- Did Claude use tools for your task? If yes, which ones?
- Did you review the tool calling?
- Did you observe variations in the two independent runs?

Ask Claude Code: "Write a Python script that analyzes all the markdown files in this
project and gives me a summary: how many files, total line count, average lines per
file, and which 5 files are the longest. Run it and show me the results." Watch how many
tool calls Claude makes and check the context cost.

**Goal:** Claude Code can write and execute scripts directly. When a task involves
processing many files or large amounts of data, this keeps context lean because only the
compact result enters the conversation, instead of the content of every file
individually.

### Exercise 2

Ask Claude Code to save the prompt from the previous exercise as a skill. It should be
called `analyze-markdown`, live in `.claude/skills/analyze-markdown/SKILL.md`, and be
manually invoked only (not auto-invoked). Review the generated SKILL.md. Check that it
has frontmatter with `name`, `description`, and `disable-model-invocation: true`.
Restart Claude Code and invoke it with `/analyze-markdown`.

**Goal:** A skill at its simplest is a saved prompt. One command instead of typing the
full prompt every time.

### Exercise 3

Ask Claude Code to update the `analyze-markdown` skill to be auto-invocable: remove the
`disable-model-invocation` flag and improve the description so Claude knows when to use
it. Restart Claude Code. Test auto-invocation by asking something like "How much
documentation does this project have?" without mentioning the skill. Watch whether
Claude loads it on its own.

**Goal:** The shift from manual to automatic invocation. The description is what Claude
reads at startup to decide when a skill is relevant. A good description makes the
difference.

### Exercise 4

In the previous exercises, Claude wrote a fresh Python script every time — the analysis
could differ between runs. Ask Claude Code to bundle a fixed script into the skill: save
the analysis script inside the skill's directory and update the SKILL.md to always run
that specific script instead of writing a new one. Test it: run it multiple times or
compare with a neighbor. Everyone should get identical results.

**Goal:** Bundling a script ensures reproducibility. Claude knows *how* to write Python
scripts; what it can't guarantee is writing the *same* script twice. This is the
difference between "Claude can do this" and "Claude does this the same way every time."

______________________________________________________________________

## MCP (Model Context Protocol)

### Exercise MCP

The key difference between an MCP server and a skill is **statefulness**. A skill runs a
script that starts, executes, and exits — each invocation is independent. An MCP server
is a long-lived process that persists between calls, which matters when you need to
maintain sessions, hold open connections, or track state across multiple interactions.

1. Set up the [Context7 MCP](https://github.com/upstash/context7) in your Claude Code
   session. Add it to `.claude/settings.local.json`:

   ```json
   {
     "mcpServers": {
       "context7": {
         "command": "npx",
         "args": ["-y", "@upstash/context7-mcp@latest"]
       }
     }
   }
   ```

1. Restart Claude Code. Run `/mcp` to verify Context7 appears in the tool list.

1. Ask Claude Code: "Using Context7, look up how to configure hooks in Claude Code."
   Observe how Claude uses the MCP tool — note the typed parameters and structured
   response.

1. Now ask a follow-up question that builds on the previous answer, e.g., "Show me an
   example for the stop event." Observe whether Context7 maintains session context
   across calls.

**Questions:**

- Could you replicate this with a skill that wraps a CLI tool? What would you lose?
- When does a long-lived, stateful server justify the extra setup compared to a simple
  skill?

______________________________________________________________________

## Subagents

### Exercise 5

TODO: There could be confusion with the built-in Explore subagent here. If we decide to
go with the readability score index, we could build a readability-improver subagent.
Same it can only read, but can give suggestions on how to improve and homogenize reading
level.

With the help of Claude Code, define a custom read-only subagent for codebase
exploration:

1. Ask Claude Code to create a subagent in `.claude/agents/` that can only read and
   search the codebase (no file edits, no Bash).
1. Review the generated markdown file — check the `tools` list, `description`, and
   `prompt`.
1. Note your current context usage.
1. Test it: ask Claude Code to use the explorer agent to answer a broad question that
   requires reading many files (e.g., *"Which files import from the utils module, and
   what do they use from it?"*).
1. Check the context usage again. The subagent may have read dozens of files, but your
   main conversation only received the summary result. Compare this to what would have
   happened if Claude had explored the codebase directly in the main conversation.
1. Verify tool restriction: ask the subagent to make a small edit to a file. It should
   not be able to.

**Goal:** Understand subagents as scoped delegation that solves two problems: context
isolation (the subagent does heavy exploration in its own context and returns only a
compact result) and safety (restricting which tools a subagent can access ensures it
can't modify anything unintended).

______________________________________________________________________

## Hooks

### Exercise 6

Create a notification hook that alerts you when Claude Code needs your input or has
finished a task:

1. Ask Claude Code: *"I want to set up a hook that notifies me whenever you need my
   input or finish a task. Can you help me create one?"*
1. Let Claude Code guide you. It should ask about your preferences (sound, visual
   banner, both?), detect your operating system, and create the hook accordingly.
1. Let Claude Code test the hook to verify it works correctly.
1. Once it works, give Claude Code a longer task and step away. See if you get notified
   in practice.

**Goal:** Experience hooks as automated lifecycle actions that run without your
intervention. Notice that hooks are configured in settings files, not in the `.claude/`
directory, and that Claude Code itself is a great tool for creating them.
