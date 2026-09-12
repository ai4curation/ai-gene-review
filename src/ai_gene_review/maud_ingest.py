#!/usr/bin/env python
"""Ingest a Maud kinetic-model TOML as candidate regulatory facts.

Maud (https://github.com/biosustain/Maud) describes a metabolic model in TOML,
including ``[[allostery]]`` and ``[[competitive_inhibition]]`` tables that encode
regulation with an explicit mechanism — exactly the layer GO cannot represent.

This module treats such a source as **evidence, not truth**: it parses the
regulatory tables into canonical :class:`~ai_gene_review.regulation_compare.RegEdge`
objects (mediated by a reviewed id-mapping), and can emit them as candidate module
``connections`` with provenance for a curator to adjudicate. It does not mutate any
curated module.
"""

from __future__ import annotations

import tomllib  # type: ignore[import-not-found]  # stdlib on py>=3.11; missing from this mypy's typeshed
from pathlib import Path
from typing import Any, Optional

import yaml

from ai_gene_review.regulation_compare import RegEdge


# (sign, mechanism) -> (connection_type, SBO id, predicate label, SBO label)
_SBO_FOR: dict[tuple[str, str], tuple[str, str, str, str]] = {
    ("+", "allosteric"): (
        "POSITIVELY_REGULATES",
        "SBO:0000636",
        "allosteric activation",
        "allosteric activator",
    ),
    ("-", "allosteric"): (
        "NEGATIVELY_REGULATES",
        "SBO:0000639",
        "allosteric inhibition",
        "allosteric inhibitor",
    ),
    ("-", "competitive"): (
        "NEGATIVELY_REGULATES",
        "SBO:0000206",
        "competitive inhibition",
        "competitive inhibitor",
    ),
}


def parse_maud_toml(path: Path | str) -> dict[str, Any]:
    """Parse a Maud TOML file into a raw dict."""
    return tomllib.loads(Path(path).read_text())


def load_mapping(path: Path | str) -> dict[str, dict[str, str]]:
    """Load a reviewed id-mapping (``enzymes:`` / ``metabolites:`` keys)."""
    data = yaml.safe_load(Path(path).read_text()) or {}
    return {
        "enzymes": data.get("enzymes") or {},
        "metabolites": data.get("metabolites") or {},
    }


def maud_regulatory_edges(
    model: dict[str, Any],
    enzyme_map: Optional[dict[str, str]] = None,
    metabolite_map: Optional[dict[str, str]] = None,
) -> set[RegEdge]:
    """Extract canonical regulatory edges from a parsed Maud model.

    ``enzyme_map`` / ``metabolite_map`` translate Maud ids to curated module
    symbols. Unmapped ids fall back to a lower-cased id so the result is still
    usable (and the mismatch is visible) without a mapping.
    """
    enzyme_map = enzyme_map or {}
    metabolite_map = metabolite_map or {}

    def enzyme(raw: Any) -> str:
        return enzyme_map.get(str(raw), str(raw).lower())

    def effector(raw: Any) -> str:
        return metabolite_map.get(str(raw), str(raw).lower())

    edges: set[RegEdge] = set()
    for entry in model.get("allostery", []):
        sign = "+" if entry.get("modification_type") == "activation" else "-"
        edges.add(
            RegEdge(
                effector(entry.get("metabolite_id")),
                enzyme(entry.get("enzyme_id")),
                sign,
                "allosteric",
            )
        )
    for entry in model.get("competitive_inhibition", []):
        edges.add(
            RegEdge(
                effector(entry.get("metabolite_id")),
                enzyme(entry.get("enzyme_id")),
                "-",
                "competitive",
            )
        )
    return edges


def candidate_connections(
    edges: set[RegEdge],
    source_id: str,
    url: Optional[str] = None,
) -> list[dict[str, Any]]:
    """Emit ingested edges as candidate module ``connections`` with provenance.

    Each connection grounds the mechanism to SBO and references the effector/enzyme
    using the module ``*_pool`` / ``*_activity`` id convention, so a curator can
    review and paste them into a module. Edges with no SBO mapping (e.g. an
    activation tagged competitive) are skipped.
    """
    connections: list[dict[str, Any]] = []
    for edge in sorted(edges, key=lambda e: (e.enzyme, e.effector)):
        spec = _SBO_FOR.get((edge.sign, edge.mechanism))
        if spec is None:
            continue
        connection_type, sbo_id, predicate_label, sbo_label = spec
        evidence: dict[str, Any] = {"source_id": source_id, "statement": f"{edge}"}
        if url:
            evidence["url"] = url
        connections.append(
            {
                "source": f"{edge.effector}_pool",
                "target": f"{edge.enzyme}_activity",
                "connection_type": connection_type,
                "predicate": {
                    "preferred_term": predicate_label,
                    "term": {"id": sbo_id, "label": sbo_label},
                },
                "evidence": [evidence],
            }
        )
    return connections


def maud_edges_from_files(
    toml_path: Path | str,
    mapping_path: Optional[Path | str] = None,
) -> set[RegEdge]:
    """Convenience: parse a Maud TOML and (optionally) a mapping into edges."""
    model = parse_maud_toml(toml_path)
    mapping = (
        load_mapping(mapping_path)
        if mapping_path
        else {"enzymes": {}, "metabolites": {}}
    )
    return maud_regulatory_edges(model, mapping["enzymes"], mapping["metabolites"])
