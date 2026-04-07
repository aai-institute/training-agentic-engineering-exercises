# Exercises: Getting Started

**Duration: 20 minutes**

For each exercise, first work through the steps, then reflect on the questions on your
own or discuss them with your neighbor.

## Exercise 1: Setup Verification

Follow these steps:

1. Ensure you are in the `01-getting-started/` directory
1. Ask Claude Code to install the Python environment
1. Ask Claude Code to verify that the installation worked

**Questions:**

- Did Claude Code complete the task without errors?
- What tools did Claude Code use to accomplish this?
- Did Claude use uv?

## Exercise 2: Hello World

Follow these steps:

1. Ask Claude Code to create a Python file that prints "Hello world!"
1. Ask Claude Code to execute the Python script.
1. Tell it to commit the changes.

**Questions:**

- Where did Claude Code put the file?
- Would you have written the commit message in the same way?

## Exercise 3: Web App

Use Claude Code to build a minimal web application using FastAPI that serves a single
page. The page should display "Hello World!" and dynamically move the text away when the
mouse cursor approaches it. Ask it to run and display the page locally. Afterwards, tell
it to commit the changes if you are satisfied.

**Questions:**

- Did you have to intervene at any point, or did the agent handle everything?
- Did you specify the font and color, or did Claude "decide" this?
- Compare your page with your neighbor's. Is Claude's output deterministic?
- Did you feel in control?
- Did you review the code before committing?

## Bonus: Exercise 4: AI-Assisted Understanding

Use Claude Code to understand Python's built-in `TopologicalSorter` class from the
`graphlib` module, using ascending levels of detail. Go through the following three
levels, each time starting with a question and continuing the conversation until you
understand the problem at that level; then continue to the next. Ask for:

- A beginner-friendly explanation using a real-world analogy (no graph theory required).

  Example: "Explain it like I've never heard of graphs; what problem does this solve in
  daily work?"

- A medium-level walkthrough with a small example you can run.

  Example: "Show me the smallest runnable example and narrate what each line does."

- An expert-level deep dive (cycles, failure modes, complexity, testing strategy).

  Example: "If I had 10,000 tasks, what should I worry about (performance/memory)?"

> **Note:** `TopologicalSorter` is part of the standard library. Claude likely knows it
> from training data and may answer from memory rather than actually reading the source
> code.

**Questions:**

- Did you learn something new?
- Did Claude Code's explanations feel accurate? How would you verify?
- Did Claude actually read the source code, or did it answer from memory? How can you
  tell?
- Could you make Claude look at the actual implementation? How?
