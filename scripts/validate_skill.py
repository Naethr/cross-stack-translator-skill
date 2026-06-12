#!/usr/bin/env python3
"""Validate the Cross-Stack Translator skill repository."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / ".agents" / "skills" / "cross-stack-translator"

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / ".gitignore",
    ROOT / "scripts" / "validate_skill.py",
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "references" / "output-template.md",
    SKILL_DIR / "references" / "stack-mappings.md",
    SKILL_DIR / "examples" / "laravel-from-express.md",
    SKILL_DIR / "examples" / "django-from-express.md",
    SKILL_DIR / "examples" / "nuxt-from-next.md",
]

FORBIDDEN_PATHS = [
    ROOT / "package.json",
    ROOT / "pyproject.toml",
    ROOT / "requirements.txt",
    ROOT / "setup.py",
    ROOT / "Dockerfile",
    ROOT / ".github" / "workflows",
    ROOT / "src",
    ROOT / "app",
    ROOT / "lib",
    ROOT / "tests",
]

REQUIRED_REPORT_SECTIONS = [
    "1. Detected stack",
    "2. Repository-specific evidence",
    "3. Mental model",
    "4. Concept mapping",
    "5. Where to start reading",
    "6. Common task walkthrough",
    "7. Things that may surprise you",
    "8. Safe first changes",
    "9. Things not to touch yet",
    "10. Unknowns and assumptions",
]

REQUIRED_MAPPING_HEADINGS = [
    "## Express + Prisma -> Laravel",
    "## Express + Prisma -> Django",
    "## Next.js -> Nuxt",
    "## Laravel -> NestJS",
]


def fail(message):
    return f"ERROR: {message}"


def read_text(path):
    return path.read_text(encoding="utf-8")


def validate_required_files(errors):
    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(fail(f"Required file is missing: {path.relative_to(ROOT)}"))


def validate_forbidden_paths(errors):
    for path in FORBIDDEN_PATHS:
        if path.exists():
            errors.append(fail(f"Forbidden path exists: {path.relative_to(ROOT)}"))


def validate_skill_front_matter(errors):
    path = SKILL_DIR / "SKILL.md"
    if not path.is_file():
        return

    text = read_text(path)
    if not text.startswith("---\n"):
        errors.append(fail("SKILL.md must start with YAML front matter."))
        return

    end = text.find("\n---", 4)
    if end == -1:
        errors.append(fail("SKILL.md YAML front matter is not closed."))
        return

    front_matter = text[4:end]
    if "name: cross-stack-translator" not in front_matter:
        errors.append(fail("SKILL.md front matter must include name: cross-stack-translator."))

    description_line = None
    for line in front_matter.splitlines():
        if line.startswith("description:"):
            description_line = line
            break

    if description_line is None:
        errors.append(fail("SKILL.md front matter must include description."))
        return

    description = description_line.lower()
    if "unfamiliar repository" not in description:
        errors.append(fail("SKILL.md description must mention an unfamiliar repository."))
    if "known stack" not in description and "stack they already know" not in description:
        errors.append(fail("SKILL.md description must mention a known stack."))


def validate_output_template(errors):
    path = SKILL_DIR / "references" / "output-template.md"
    if not path.is_file():
        return

    text = read_text(path)
    for section in REQUIRED_REPORT_SECTIONS:
        if section not in text:
            errors.append(fail(f"output-template.md is missing section: {section}"))


def validate_stack_mappings(errors):
    path = SKILL_DIR / "references" / "stack-mappings.md"
    if not path.is_file():
        return

    text = read_text(path)
    for heading in REQUIRED_MAPPING_HEADINGS:
        if heading not in text:
            errors.append(fail(f"stack-mappings.md is missing heading: {heading}"))


def main():
    errors = []
    validate_required_files(errors)
    validate_forbidden_paths(errors)
    validate_skill_front_matter(errors)
    validate_output_template(errors)
    validate_stack_mappings(errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Cross-Stack Translator skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
