# Exericse: Tools and Capabilities

## Exercise 1: Calculating reading-ease scores

The Flesch-Kincaid readability tests indicate how easy an English text is to understand,
and are used to evaluate technical documentation. In this exercise, we will use this
methodology to evaluate the reading-ease of our exercise instructions.

1. Ensure you are in the `05-tools-and-capabilities/` directory.
1. Prompt Claude Code to calculate the Flesch-Kincaid reading-ease score this chapters
   `README.md`. Carefully monitor what Claude Code does. (*For background on the
   Flesch-Kincaid readability test consider its
   [Wikipedia entry](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests).*)
1. Tell Claude to write down the score in a text file using the schema
   `file_path: score`.
1. Clear the context, then run the same prompt again, but this time calculate the score
   of the `README.md` file inside the `03-customization` directory.
1. Save the score to the text file from above.
1. Given the calculated scores, ask Claude which README file is easier to read.

**Reflections:**

- Did Claude create helper scripts or similar artifacts to solve the problem?
- To compare the two scores we need to ensure that they have been calculated using the
  same method.
  1. Can we do this here?
  1. Does your answer change if we wouldn't have cleared the context?
- What could we do to increase reproducibility between runs?

## Exercise 2: Writing your first skill

Continue in the session from Exercise 1.

### 2.1 The interview

Re-read the slide "Writing Your First Skill". The following requirements are the
*"intent"*. Given those, let Claude Code interview you (maximum 3 questions; one at a
time). You don't need to test the skill here, we will do that in Exercise 2.2.

- The skill should be called `flesch-kincaid`
- You want the skill to only work for specific markdown files like so:
  ```console
  /flesch-kincaid ../03-customization/README.md
  ```
- You want a script that deterministically computes the reading-ease score for a
  markdown file, and that the skill always uses it.
- You want the output of the skill to be
  ```markdown
  The Flesch-Kincaid reading-ease score for {path/to/markdown-file} is {score}.
  ```
- The skill should live in the `05-tools-and-capabilities/.claude/` folder.

**Reflections:**

- Did the interview uncover edge cases that were not covered by the requirements?

### 2.2 The first draft

Continue in the session from Exercise 2.1.

1. Now ask Claude Code to write a skill given the result of the interview. Continue the
   conversation until you have a first draft of the skill.
1. Close the session and start a new one (this is required so that the skill is loaded).
1. Test the skill by running it on the `README.md` file of this chapter:
   ```console
   /flesch-kincaid README.md
   ```
1. Compare the skill-generated score to the persisted one from Exercise 1.

**Important:** If you don't have a working skill by now, you can find a solution in the
folder `../fallback`. Use this implementation for this and the remaining exercises.
Handle it, as if it were a third-party skill!

**Reflection:**

- Look at the created `SKILL.md` file. Does it fulfill the requirements listed in
  Exercise 2.1?
- Is the skill auto-invokable?

## Exercise 3: Auto-invoking your skill

While chatting with Claude you realized that it should sometimes invoke the skill
automatically, for example, when talking about the reading-ease of a text.

1. Ensure that the skill is auto-invokable (see the slide 'Manual and Auto Invocation')
1. In a new session, prompt Claude Code with the following:
   ```markdown
   Compare the readability of this chapters README.md with that of ../03-customization/README.md
   ```

**Reflection:**

- For this type of skill, do you want to allow auto-invocation at all?
- What would you do if the skill wouldn't have been triggered?
