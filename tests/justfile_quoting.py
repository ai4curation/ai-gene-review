"""Shared assertions for shell-path interpolation in project justfiles."""

from __future__ import annotations

import re
from collections.abc import Collection


INTERPOLATION = re.compile(r"\{\{(?P<body>[^{}]+)\}\}")


def find_unquoted_recipe_path_interpolations(
    text: str, path_names: Collection[str]
) -> list[str]:
    """Return recipe-line path interpolations that do not start inside a quote."""
    normalized_path_names = {re.sub(r"\s+", "", name) for name in path_names}
    unquoted: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line[:1].isspace():
            continue
        for match in INTERPOLATION.finditer(line):
            normalized_name = re.sub(r"\s+", "", match.group("body"))
            if normalized_name not in normalized_path_names:
                continue
            if match.start() == 0 or line[match.start() - 1] not in {'"', "'"}:
                unquoted.append(f"line {line_number}: {match.group(0)}")
    return unquoted
