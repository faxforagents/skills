#!/usr/bin/env python3
"""Check every skills/*/SKILL.md against the Agent Skills frontmatter rules (agentskills.io/specification).

Standard library only, so it runs on any CI runner.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("no frontmatter")
    end = text.index("\n---\n", 4)
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line or line.startswith(" "):
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    problems: list[str] = []
    paths = sorted(root.glob("skills/*/SKILL.md"))
    if not paths:
        problems.append("no skills/*/SKILL.md found")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        try:
            fields = frontmatter(text)
        except ValueError as err:
            problems.append(f"{path}: {err}")
            continue
        name = fields.get("name", "")
        description = fields.get("description", "")
        if not NAME_RE.match(name) or len(name) > 64:
            problems.append(f"{path}: name {name!r} must be 1-64 lowercase letters, digits and single hyphens")
        if name != path.parent.name:
            problems.append(f"{path}: name {name!r} must match the folder {path.parent.name!r}")
        if not 1 <= len(description) <= 1024:
            problems.append(f"{path}: description must be 1-1024 characters, got {len(description)}")
        compat = fields.get("compatibility")
        if compat is not None and not 1 <= len(compat) <= 500:
            problems.append(f"{path}: compatibility must be 1-500 characters")
        body_lines = text.count("\n")
        if body_lines > 500:
            problems.append(f"{path}: {body_lines} lines, the format recommends 500 or fewer")
    for problem in problems:
        print(f"check_skill: FAIL: {problem}", file=sys.stderr)
    if not problems:
        print(f"check_skill: OK ({len(paths)} skill)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
