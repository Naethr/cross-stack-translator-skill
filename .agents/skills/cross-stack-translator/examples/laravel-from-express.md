# Example: Laravel from Express

## Example user prompt

"I know Express and Prisma. Help me understand this Laravel repo so I can make a small API change."

## What the skill should inspect

- Top-level files and directories.
- `composer.json` if present.
- Laravel route files such as `routes/api.php` and `routes/web.php` if present.
- Controllers under `app/Http/Controllers` if present.
- Models under `app/Models` if present.
- Migrations under `database/migrations` if present.
- Test configuration or test directories if present.

## What a good answer should include

- Verified Laravel evidence from actual files.
- A route-handler mental model that compares Express routes to Laravel routes and controllers.
- A data-layer comparison between Prisma and Eloquent, with active record differences called out.
- A safe reading path for the user's API-change goal.
- Unknowns where the repo does not show enough evidence.

## What a bad answer would do

- Give a generic Laravel tutorial.
- Claim the project uses Eloquent, queues, policies, or Sanctum without file evidence.
- Recommend refactors before explaining the current structure.
- Generate code for the API change before being asked.

## Why this is stack translation, not generic onboarding

The answer explains Laravel through the user's Express and Prisma mental model, using repository files as evidence. It focuses on the concepts needed to navigate the repo, not a broad summary of every directory.
