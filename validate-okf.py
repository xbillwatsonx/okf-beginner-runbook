#!/usr/bin/env python3
"""Tiny OKF Markdown validator with no external dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
BAD_PATH_RE = re.compile(r"(^|[(/\\])([A-Za-z]:\\|/home/)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate basic OKF Markdown frontmatter and portable links."
    )
    parser.add_argument("folder", help="Path to an OKF knowledge base folder")
    return parser.parse_args()


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def has_content(path: Path) -> bool:
    return bool(path.read_text(encoding="utf-8").strip())


def check_frontmatter(path: Path, root: Path, failures: list[str]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    name = rel(path, root)

    if not lines or lines[0] != "---":
        failures.append(f"{name}: missing opening frontmatter line '---'")
        return

    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        failures.append(f"{name}: missing closing frontmatter line '---'")
        return

    body = lines[1:end]
    type_lines = [line for line in body if line.startswith("type:")]
    if not type_lines:
        failures.append(f"{name}: missing root-level type field")
        return

    value = type_lines[0].split(":", 1)[1].strip().strip("\"'")
    if not value:
        failures.append(f"{name}: type field is empty")


def check_links(path: Path, root: Path, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        clean = target.split("#", 1)[0].strip()
        if BAD_PATH_RE.search(clean):
            failures.append(f"{rel(path, root)}: machine-specific link path: {target}")


def validate(root: Path) -> list[str]:
    failures: list[str] = []

    if not root.exists() or not root.is_dir():
        return [f"{root}: folder does not exist"]

    for required in ("index.md", "log.md"):
        path = root / required
        if not path.exists():
            failures.append(f"{required}: missing at root")
        elif not has_content(path):
            failures.append(f"{required}: exists but is empty")

    for path in sorted(root.rglob("*.md")):
        name = path.name.lower()
        if name in {"index.md", "log.md"}:
            if not has_content(path):
                failures.append(f"{rel(path, root)}: reserved file is empty")
        else:
            check_frontmatter(path, root, failures)
        check_links(path, root, failures)

    return failures


def main() -> int:
    args = parse_args()
    root = Path(args.folder).expanduser().resolve()
    failures = validate(root)

    if failures:
        print(f"FAIL: {len(failures)} issue(s) found in {root}")
        for failure in failures:
            print(f"- {failure}")
        return 1

    total = sum(1 for _ in root.rglob("*.md"))
    print(f"PASS: checked {total} Markdown file(s) in {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
