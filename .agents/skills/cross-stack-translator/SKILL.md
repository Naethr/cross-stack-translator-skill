---
name: cross-stack-translator
description: Use when a developer needs to understand an unfamiliar repository by mapping its framework concepts, file structure, conventions, and common workflows to a stack they already know. Not for generic codebase summaries.
---

# Cross-Stack Translator

Use this skill to help a developer understand an unfamiliar repository through a stack they already know. The output is a repository-grounded translation, not a generic framework tutorial.

This skill requires no runtime dependencies.

## Operating Rules

- Ask for the user's known stack if it is not stated.
- Infer the user's known stack only when the prompt gives clear evidence.
- Ask for the user's immediate goal when it would change what to inspect or explain.
- Inspect repository structure before explaining.
- Identify language, framework, package manager, database or ORM layer, test framework, and build tools when repository evidence allows it.
- Ground every explanation in files actually found in the repository.
- Map concepts from the user's known stack to concepts in the current repository.
- Produce the stable output format named "Stack Translation Report".
- Clearly separate verified facts from assumptions.
- List unknowns when evidence is incomplete.
- Avoid generic framework tutorials.
- Avoid code modifications.
- Avoid destructive commands.
- Avoid dependency installation.
- Avoid running migrations.
- Avoid claiming certainty when repository evidence is incomplete.

## Required Workflow

1. Establish the known stack.
   - Use the user's explicit statement when available.
   - If not available, ask a concise question before producing the report.

2. Clarify the immediate goal when useful.
   - Examples: routing, data model, authentication, tests, local development flow, or feature work.
   - If no goal is provided, produce a broad but concise first-pass translation.

3. Inspect the repository.
   - Start with file and directory structure.
   - Then inspect the smallest useful set of configuration, routing, model, controller, page, test, and build files.
   - Do not claim to inspect files that were not inspected.

4. Identify the detected stack.
   - Include only what is supported by repository evidence.
   - Mark incomplete or ambiguous findings as unknown.

5. Translate concepts.
   - Explain unfamiliar concepts using the user's known stack.
   - Prefer practical equivalences over theory.
   - Call out important differences where a direct equivalence would be misleading.

6. Produce the report.
   - Use the sections from `references/output-template.md`.
   - Keep the format stable.
   - Keep the content specific to the repository.

## Must Not Do

- Do not summarize the repository generically.
- Do not explain the framework without referencing actual repository files.
- Do not claim to inspect files you did not inspect.
- Do not recommend refactors before understanding the repository.
- Do not suggest deleting or rewriting code.
- Do not generate implementation code unless the user explicitly asks in a later step.
- Do not act as a security auditor.
- Do not act as a dead-code detector.
- Do not act as a performance analyzer.
- Do not act as a dependency upgrade assistant.

## Reference Files

- Use `references/output-template.md` for the report structure.
- Use `references/stack-mappings.md` only as initial mapping guidance. Repository evidence takes priority.
