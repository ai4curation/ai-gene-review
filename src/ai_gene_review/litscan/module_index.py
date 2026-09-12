"""Build a match index from the curated ``modules/`` knowledge base."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class ModuleEntity:
    """A module flattened into the terms and references litscan needs."""

    id: str
    title: str
    path: str
    terms: list[str] = field(default_factory=list)  # candidate names, deduped, ordered
    cited_pmids: set[str] = field(default_factory=set)  # {"PMID:123", ...}

    @property
    def known_terms_lower(self) -> set[str]:
        return {t.casefold() for t in self.terms}


def _normalize_pmid(value: str) -> str | None:
    if value.upper().startswith("PMID:"):
        digits = re.sub(r"\D", "", value.split(":", 1)[1])
        return f"PMID:{digits}" if digits else None
    return None


def _collect(
    node: Any, preferred: list[str], labels: list[str], pmids: set[str]
) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "preferred_term" and isinstance(value, str):
                preferred.append(value)
            elif key == "source_id" and isinstance(value, str):
                pmid = _normalize_pmid(value)
                if pmid:
                    pmids.add(pmid)
            elif key == "term" and isinstance(value, dict):
                label = value.get("label")
                if isinstance(label, str):
                    labels.append(label)
            _collect(value, preferred, labels, pmids)
    elif isinstance(node, list):
        for item in node:
            _collect(item, preferred, labels, pmids)


def module_entity_from_doc(doc: dict[str, Any], path: Path) -> ModuleEntity:
    """Flatten one parsed module document into a :class:`ModuleEntity`."""
    preferred: list[str] = []
    labels: list[str] = []
    pmids: set[str] = set()
    _collect(doc, preferred, labels, pmids)

    title = str(doc.get("title") or path.stem.replace("_", " "))
    module_label = ""
    module = doc.get("module")
    if isinstance(module, dict) and isinstance(module.get("label"), str):
        module_label = module["label"]

    seen: set[str] = set()
    terms: list[str] = []
    for candidate in [title, module_label, *preferred, *labels]:
        candidate = candidate.strip()
        key = candidate.casefold()
        if candidate and key not in seen:
            seen.add(key)
            terms.append(candidate)

    return ModuleEntity(
        id=str(doc.get("id") or path.stem),
        title=title,
        path=str(path),
        terms=terms,
        cited_pmids=pmids,
    )


def load_modules(modules_dir: Path) -> list[ModuleEntity]:
    """Load every ``modules/*.yaml`` (skipping deep-research sidecars) into entities."""
    entities: list[ModuleEntity] = []
    for path in sorted(modules_dir.glob("*.yaml")):
        if "deep-research" in path.name:
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if isinstance(doc, dict) and (doc.get("module") or doc.get("id")):
            entities.append(module_entity_from_doc(doc, path))
    return entities
