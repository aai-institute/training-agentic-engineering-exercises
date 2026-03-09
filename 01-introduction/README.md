# 1. Getting Started

## Exercise 1

Open Claude Code and tell it to clone the [...] repo to an appropriate directory, as
well as to install the Python environment. Afterwards, ask it to verify that the Python
installation has worked.

**Goal:** Ensure that Claude Code works, and the Python installation (via `uv`) is
functional.

## Exercise 2

Let Claude Code create and execute a Python script that prints "Hello world!" in the
terminal. Afterwards, commit the changes.

**Goal:** (1) Ensure their Python installation can execute code; (2) First positive
experience with code generation.

## Exercise 3

Use Claude Code to build a minimal web application using FastAPI that serves a single
page. The page should display "Hello World!" and dynamically move the text away when the
mouse cursor approaches it. Ask it to run and display the page locally. Afterwards,
commit the changes.

**Goal:** First positive experience with advanced code generation.

## Exercise 4

Use Claude Code to understand Python's built-in `TopologicalSorter` class from the
`graphlib` module, using ascending levels of detail. Go through the following three
levels, each time starting with a question and continuing the conversation until you
understand the problem at that level; then continue to the next. Ask for:

- A beginner-friendly explanation using a real-world analogy (no graph theory required).
- A medium-level walkthrough with a small example you can run.
- An expert-level deep dive (cycles, failure modes, complexity, testing strategy).

Example follow-up questions (use across the three passes):

- "Explain it like I've never heard of graphs; what problem does this solve in daily
  work?"
- "Show me the smallest runnable example and narrate what each line does."
- "What exactly counts as a cycle here, and how would I detect/report it nicely?"
- "If I had 10,000 tasks, what should I worry about (performance/memory)?"

**Goal:** (1) First AI-assisted code understanding experience; (2) Have an open question
so that advanced students are kept busy / interested.
