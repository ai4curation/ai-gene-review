"""Evaluate and check curated annotation rules (rules/curated/CR-*.yaml).

A curated rule couples sequence-feature conditions (InterPro, Pfam, PANTHER,
FunFam, CDD, NCBIfam) with taxon and module-context conditions. It fires for a
protein when ANY condition set holds, and a set holds when ALL its conditions
hold. ``MODULE_CONTEXT`` conditions are exclusion-only: they fail only when the
module is known to be unsatisfiable in the protein's context, so a detection gap
never suppresses an annotation.

>>> rule = {"condition_sets": [{"number": 1, "conditions": [
...     {"condition_type": "INTERPRO", "value": "IPR005024"},
...     {"condition_type": "TAXON", "value": "NCBITaxon:2759"}]}]}
>>> rule_fires(rule, ProteinFeatures({"INTERPRO": {"IPR005024"}}, {"NCBITaxon:2759"}))
True
>>> rule_fires(rule, ProteinFeatures({"INTERPRO": {"IPR005024"}}, {"NCBITaxon:2157"}))
False
>>> to_uniprot_query(rule)
'(xref:interpro-IPR005024 AND taxonomy_id:2759)'

Run ``python -m ai_gene_review.curated_rules check rules/curated/CR-*.yaml`` to check
rules, adding ``--count`` to report UniProtKB match counts (network).
"""

from __future__ import annotations

import argparse
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Mapping, Optional

import yaml

CURATED_RULES_DIR = Path("rules/curated")

SEQUENCE_CONDITIONS = ("INTERPRO", "PFAM", "PANTHER", "FUNFAM", "CDD", "NCBIFAM")

# UniProt query field for each sequence-feature condition type. FunFam ids are not
# a UniProt cross-reference field, so they are matched as a quoted text search.
UNIPROT_XREF = {
    "INTERPRO": "interpro",
    "PFAM": "pfam",
    "PANTHER": "panther",
    "CDD": "cdd",
    "NCBIFAM": "ncbifam",
}


@dataclass
class ProteinFeatures:
    """What a rule is tested against: a protein's signatures and its lineage.

    Attributes:
        signatures: accessions by condition type, e.g. ``{"INTERPRO": {"IPR005024"}}``
        taxon_ids: NCBITaxon CURIEs of the organism's full lineage
    """

    signatures: dict[str, set[str]] = field(default_factory=dict)
    taxon_ids: set[str] = field(default_factory=set)


def condition_holds(
    condition: dict,
    features: ProteinFeatures,
    module_context: Optional[Mapping[str, Optional[bool]]] = None,
) -> bool:
    """Test one condition.

    ``module_context`` maps a ``MODULE:`` id to True (satisfiable), False
    (unsatisfiable) or None (not evaluated).

    >>> f = ProteinFeatures({"CDD": {"cd23940"}}, {"NCBITaxon:2157"})
    >>> condition_holds({"condition_type": "CDD", "value": "cd23940"}, f)
    True
    >>> condition_holds({"condition_type": "MODULE_CONTEXT", "value": "MODULE:x"}, f, {"MODULE:x": False})
    False
    """
    ctype = condition["condition_type"]
    value = condition["value"]
    if ctype == "MODULE_CONTEXT":
        return (module_context or {}).get(value) is not False
    if ctype == "TAXON":
        present = value in features.taxon_ids
    else:
        present = value in features.signatures.get(ctype, set())
    return not present if condition.get("negated") else present


def rule_fires(
    rule: dict,
    features: ProteinFeatures,
    module_context: Optional[Mapping[str, Optional[bool]]] = None,
) -> bool:
    """True when any condition set of ``rule`` holds for ``features``."""
    return any(
        all(condition_holds(c, features, module_context) for c in cs["conditions"])
        for cs in rule["condition_sets"]
    )


def _query_clause(condition: dict) -> Optional[str]:
    """UniProt query clause for one condition, or None for module conditions."""
    ctype = condition["condition_type"]
    value = condition["value"]
    if ctype == "MODULE_CONTEXT":
        return None
    if ctype == "TAXON":
        clause = f"taxonomy_id:{value.removeprefix('NCBITaxon:')}"
    elif ctype == "FUNFAM":
        clause = f'"{value}"'
    else:
        clause = f"xref:{UNIPROT_XREF[ctype]}-{value}"
    return f"NOT {clause}" if condition.get("negated") else clause


def to_uniprot_query(rule: dict) -> str:
    """UniProtKB query equivalent to the rule's sequence and taxon conditions.

    Module-context conditions cannot be expressed as a query and are omitted, so
    the query is an upper bound on what the rule annotates.
    """
    sets = []
    for cs in rule["condition_sets"]:
        clauses = [c for c in (_query_clause(x) for x in cs["conditions"]) if c]
        sets.append("(" + " AND ".join(clauses) + ")")
    return " OR ".join(sets)


@lru_cache(maxsize=8)
def _module_ids(modules_dir: Path) -> frozenset[str]:
    """``MODULE:`` ids of the module documents in ``modules_dir`` (cached per directory)."""
    ids = set()
    for path in modules_dir.glob("*.yaml"):
        with open(path) as f:
            doc = yaml.safe_load(f)
        if isinstance(doc, dict) and isinstance(doc.get("id"), str):
            ids.add(doc["id"])
    return frozenset(ids)


def check_rule(rule: dict, modules_dir: Path = Path("modules")) -> list[str]:
    """Semantic checks beyond the schema. Returns a list of error messages.

    - every condition set has at least one non-negated sequence-feature condition;
    - MODULE_CONTEXT conditions are not negated and name an existing module;
    - TAXON values are NCBITaxon CURIEs.
    """
    errors = []
    module_ids: Optional[frozenset[str]] = None
    for cs in rule["condition_sets"]:
        label = f"{rule.get('id', '?')} set {cs.get('number')}"
        anchors = [
            c for c in cs["conditions"]
            if c["condition_type"] in SEQUENCE_CONDITIONS and not c.get("negated")
        ]
        if not anchors:
            errors.append(f"{label}: no sequence-feature condition anchors the set")
        for c in cs["conditions"]:
            if c["condition_type"] == "TAXON" and not c["value"].startswith("NCBITaxon:"):
                errors.append(f"{label}: TAXON value {c['value']!r} is not an NCBITaxon CURIE")
            if c["condition_type"] == "MODULE_CONTEXT":
                if c.get("negated"):
                    errors.append(f"{label}: MODULE_CONTEXT cannot be negated (exclusion-only)")
                if module_ids is None:
                    module_ids = _module_ids(modules_dir)
                if c["value"] not in module_ids:
                    errors.append(f"{label}: unknown module {c['value']!r}")
    return errors


def count_uniprot(query: str) -> int:
    """Number of UniProtKB entries matching ``query`` (network)."""
    params = urllib.parse.urlencode({"query": query, "size": 1, "format": "list"})
    url = f"https://rest.uniprot.org/uniprotkb/search?{params}"
    with urllib.request.urlopen(url, timeout=60) as resp:
        return int(resp.headers["X-Total-Results"])


def main(argv: Optional[list[str]] = None) -> int:
    """CLI: ``check FILE... [--count]``. Exit status 1 if any rule has errors."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check", help="semantic check of curated rule files")
    check.add_argument("files", nargs="+", type=Path)
    check.add_argument("--count", action="store_true", help="report UniProtKB match counts")
    check.add_argument("--modules-dir", type=Path, default=Path("modules"))
    args = parser.parse_args(argv)

    failed = False
    for path in args.files:
        with open(path) as f:
            rule = yaml.safe_load(f)
        errors = check_rule(rule, args.modules_dir)
        status = "✗" if errors else "✓"
        print(f"{status} {path}")
        for e in errors:
            print(f"  {e}")
        failed |= bool(errors)
        if args.count:
            query = to_uniprot_query(rule)
            print(f"  query: {query}")
            print(f"  UniProtKB matches (module conditions not applied): {count_uniprot(query)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
