# Cross-Stack Translator

Understand unfamiliar codebases through the stack you already know.

Cross-Stack Translator is an instruction-only Agent Skill that helps developers orient themselves in unfamiliar repositories by mapping framework concepts, file structure, conventions, and common workflows to a stack they already know.

It is designed as a practical orientation aid. It does not guarantee correctness, completeness, safety, or suitability for any specific project.

## What the skill does

* Asks for, or infers, the user's known stack.
* Inspects the repository structure before explaining.
* Grounds explanations in files actually present in the repository.
* Maps unfamiliar concepts to familiar stack concepts.
* Produces a structured Stack Translation Report.
* Separates verified facts, assumptions, and unknowns.
* Helps the user decide where to start reading before making changes.

## What the skill does not do

* It does not modify code.
* It does not install dependencies.
* It does not run migrations.
* It does not execute destructive commands.
* It does not act as a generic repository summarizer.
* It does not act as a code reviewer, security auditor, performance analyzer, legal advisor, or dependency upgrade assistant.
* It does not detect dead code.
* It does not guarantee that its interpretation of a repository is correct or complete.
* It does not replace human review, project documentation, tests, maintainers, or professional judgment.
* It does not generate implementation code unless explicitly asked in a later step.

## Important limitations

Cross-Stack Translator relies on the repository files available to the agent and on the agent's interpretation of those files. Its output may be incomplete, outdated, incorrect, or misleading.

Before relying on its output, users should verify important claims against the actual repository, documentation, tests, maintainers, and runtime behavior.

Do not use this skill as the sole basis for production changes, security decisions, architecture decisions, migrations, deletions, or client commitments.

## Example usage prompts

* "I know Express and Prisma. Help me understand this Laravel repo."
* "I come from Express and Prisma. Translate this Django project for me."
* "I know Next.js. Explain this Nuxt repo through that mental model."

## Current MVP scope

The MVP contains concise, practical mappings for:

* Express + Prisma to Laravel
* Express + Prisma to Django
* Next.js to Nuxt
* Laravel to NestJS

These mappings are intentionally limited and may be incomplete. The skill should not claim broader framework support than the mappings and examples currently included.

## Repository structure

```text
cross-stack-translator/
  AGENTS.md
  README.md
  LICENSE
  .gitignore
  scripts/
    validate_skill.py
  .agents/
    skills/
      cross-stack-translator/
        SKILL.md
        references/
          output-template.md
          stack-mappings.md
        examples/
          laravel-from-express.md
          django-from-express.md
          nuxt-from-next.md
```

## Validation

Run:

```bash
python3 scripts/validate_skill.py
```

On systems where `python` points to Python 3, `python scripts/validate_skill.py` may also work.

Validation only checks the repository structure and basic skill files. It does not prove that the skill is correct, complete, safe, or suitable for any particular codebase.

## Project status

This project is instruction-only for now. It contains no app, CLI, backend, frontend, API, database layer, publishable package, runtime scanning engine, or code modification engine.

## License

MIT.

This project is provided "as is", without warranty of any kind. See the [LICENSE](LICENSE) file for details.
