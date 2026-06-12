# Example: Nuxt from Next.js

## Example user prompt

"I know Next.js. Help me understand this Nuxt repo before I edit a page."

## What the skill should inspect

- Top-level files and directories.
- `package.json` if present in the target repository being analyzed.
- `nuxt.config.*` if present.
- `pages`, `layouts`, `components`, `composables`, and `server` directories if present.
- Data-fetching patterns in representative page files.
- Test or build configuration if present.

## What a good answer should include

- Verified Nuxt evidence from actual files.
- A routing comparison between Next.js and Nuxt file-based routing.
- A layout and page mental model grounded in files found in the repo.
- Differences around server routes, rendering, and data fetching where file evidence exists.
- A safe reading path for editing a page.

## What a bad answer would do

- Give a generic Nuxt tutorial.
- Assume the repo uses every Nuxt convention.
- Treat Nuxt as a one-to-one clone of Next.js.
- Generate Vue code before the user asks for implementation.

## Why this is stack translation, not generic onboarding

The answer starts from the user's Next.js knowledge and translates the inspected Nuxt structure into comparable concepts. It is useful because it reduces unfamiliarity without pretending the frameworks are identical.
