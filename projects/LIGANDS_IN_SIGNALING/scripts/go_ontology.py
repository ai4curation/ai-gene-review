"""Minimal GO OBO reader shared by the ligand gap scripts.

Reads term names, is_a and part_of edges and obsolete flags from an OBO file
(go-basic.obo is enough: it keeps is_a and part_of within an aspect).
"""
from __future__ import annotations

import collections
from functools import lru_cache
from pathlib import Path


class GO:
    def __init__(self, obo_path: Path):
        self.name: dict[str, str] = {}
        self.is_a: dict[str, set[str]] = collections.defaultdict(set)
        self.part_of: dict[str, set[str]] = collections.defaultdict(set)
        self.obsolete: set[str] = set()
        current = None
        for line in open(obo_path):
            line = line.rstrip("\n")
            if line == "[Term]":
                current = None
                continue
            if line.startswith("[Typedef]"):
                current = "TYPEDEF"
                continue
            if current == "TYPEDEF":
                continue
            if line.startswith("id: GO:"):
                current = line[4:]
            elif current and line.startswith("name: "):
                self.name[current] = line[6:]
            elif current and line.startswith("is_a: "):
                self.is_a[current].add(line[6:16])
            elif current and line.startswith("relationship: part_of "):
                self.part_of[current].add(line[22:32])
            elif current and line == "is_obsolete: true":
                self.obsolete.add(current)
        self.data_version = next(
            (l.split(": ", 1)[1].strip() for l in open(obo_path) if l.startswith("data-version")), "unknown"
        )

    @lru_cache(maxsize=None)
    def ancestors(self, term: str, with_part_of: bool = False) -> frozenset[str]:
        """Reflexive ancestors over is_a (and part_of if requested)."""
        out = {term}
        parents = set(self.is_a.get(term, ()))
        if with_part_of:
            parents |= self.part_of.get(term, set())
        for p in parents:
            out |= self.ancestors(p, with_part_of)
        return frozenset(out)

    def is_a_descendant(self, term: str, ancestor: str) -> bool:
        return ancestor in self.ancestors(term)

    def descendants_of_any(self, roots: set[str]) -> set[str]:
        return {t for t in self.name if t not in self.obsolete and self.ancestors(t) & roots}
