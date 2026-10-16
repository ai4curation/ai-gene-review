"""One conservative rule for symbols used by module reasoning and validation."""

from __future__ import annotations

import re
from typing import Any

_SYMBOL_TOKEN = r"[A-Za-z0-9][A-Za-z0-9_.:/-]*"
_SYMBOL_LABEL = re.compile(
    rf"({_SYMBOL_TOKEN})(?:\s+/\s+{_SYMBOL_TOKEN})*(?:\s+\(.*\)(?:,\s+.+)?)?",
    re.DOTALL,
)


def descriptor_symbol(descriptor: dict) -> str | None:
    """Read the primary symbol, allowing explicit aliases and parenthetical qualifiers.

    >>> descriptor_symbol({"preferred_term": "MetXS (PSEPK)"})
    'MetXS'
    >>> descriptor_symbol({"preferred_term": "SLC25A4 / ANT1 (human)"})
    'SLC25A4'
    >>> descriptor_symbol({"preferred_term": "PSEPK MetXS"}) is None
    True
    """
    label = descriptor.get("preferred_term")
    if not isinstance(label, str):
        return None
    match = _SYMBOL_LABEL.fullmatch(label.strip())
    return match[1].rstrip(":") if match else None


def symbol_label_warnings(document: Any) -> list[str]:
    """Report descriptors that cannot safely participate in symbol predicates.

    Accessions remain usable, so these are advisory validation findings rather
    than invalidating otherwise grounded modules. Runtime extraction nevertheless
    refuses every ambiguous label, whether or not validation was run first.
    """
    warnings: list[str] = []

    def check(descriptor: Any, path: str) -> None:
        if isinstance(descriptor, dict) and descriptor_symbol(descriptor) is None:
            warnings.append(
                f"SYMBOL_LABEL {path}: {descriptor.get('preferred_term')!r} is not "
                "symbol-first. Use SYMBOL, SYMBOL / ALIAS, or either with (organism/description), after "
                "verifying the symbol; no symbol is inferred from this label. "
                "UniProt accession predicates remain available."
            )

    def walk(value: Any, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                child_path = f"{path}.{key}" if path else key
                if key == "gene":
                    check(child, child_path)
                elif key == "representative_members" and isinstance(child, list):
                    for index, member in enumerate(child):
                        check(member, f"{child_path}[{index}]")
                walk(child, child_path)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")

    walk(document, "")
    return warnings
