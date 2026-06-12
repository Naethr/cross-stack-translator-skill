# Example: Django from Express

## Example user prompt

"I usually build Express and Prisma apps. Translate this Django project structure for me."

## What the skill should inspect

- Top-level files and directories.
- Dependency or project files such as `requirements.txt`, `pyproject.toml`, or `manage.py` if present in the target repository being analyzed.
- Django settings modules if present.
- URL configuration files such as `urls.py` if present.
- App directories containing `models.py`, `views.py`, `serializers.py`, or `tests.py` if present.
- Migration directories if present.

## What a good answer should include

- Verified Django evidence from actual files.
- A mapping from Express routes to Django URL configuration and views.
- A mapping from Prisma schema and migrations to Django models and migrations.
- Differences between request handling in Express middleware and Django middleware.
- Unknowns where the repository does not provide enough evidence.

## What a bad answer would do

- Explain Django as if every project uses Django REST Framework.
- Claim a database, ORM usage pattern, or test framework without evidence.
- Ignore the user's Express and Prisma background.
- Summarize folders without translating concepts.

## Why this is stack translation, not generic onboarding

The answer uses Express and Prisma as the comparison frame. It teaches the user how to transfer existing mental models to the inspected Django repo instead of producing a generic project tour.
