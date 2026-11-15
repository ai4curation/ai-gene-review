"""Tally the description-text source defects recorded by the MOD descriptions project.

Counts the WRONG_STATEMENT, OUTDATED_STATEMENT and MISSING_STATEMENT defects (and
WRONG_REFERENCE defects on a cited file) recorded on the cited MOD and UniProt
description files of the worm, yeast and fly reviews, and lists each one with its
quoted source sentence and first piece of evidence. Other source defects, mostly on
GO annotations, are not counted.

Usage:
    uv run python projects/MOD_DESCRIPTIONS/defect_tally.py -o projects/MOD_DESCRIPTIONS/defect-tally.yaml
"""

import argparse
import collections
from datetime import date
from pathlib import Path
from typing import Any, Dict, Iterator, List

import yaml

ORGANISMS = ("worm", "yeast", "DROME")
STATEMENT_TYPES = ("WRONG_STATEMENT", "OUTDATED_STATEMENT", "MISSING_STATEMENT")


def iter_defects(genes_dir: Path) -> Iterator[Dict[str, Any]]:
    """Yield one row per description-text defect in the worm, yeast and fly reviews."""
    for org in ORGANISMS:
        for review in sorted((genes_dir / org).glob("*/*-ai-review.yaml")):
            data = yaml.safe_load(review.read_text(encoding="utf-8")) or {}
            for ref in data.get("references") or []:
                ref_id = str(ref.get("id", ""))
                for sd in (ref.get("reference_review") or {}).get("source_defects") or []:
                    kind = str(sd.get("defect_type", ""))
                    if kind not in STATEMENT_TYPES and not (kind == "WRONG_REFERENCE" and ref_id.startswith("file:")):
                        continue
                    evidence = (sd.get("supported_by") or [{}])[0]
                    yield {
                        "organism": org,
                        "gene": review.parent.name,
                        "resource": sd.get("resource"),
                        "defect_type": kind,
                        "confidence": sd.get("confidence"),
                        "record": sd.get("record"),
                        "asserted_value": sd.get("asserted_value"),
                        "explanation": sd.get("explanation"),
                        "evidence_reference": evidence.get("reference_id"),
                        "evidence_text": evidence.get("supporting_text"),
                    }


def summarise(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Count defects by organism and resource, type and confidence."""
    by_org: Dict[str, Dict[str, int]] = collections.defaultdict(lambda: collections.defaultdict(int))
    for r in rows:
        by_org[r["organism"]][r["resource"]] += 1
    mods = {"WORMBASE", "SGD", "FLYBASE"}
    return {
        "date": date.today().isoformat(),
        "total": len(rows),
        "mod_text": sum(1 for r in rows if r["resource"] in mods),
        "uniprot_text": sum(1 for r in rows if r["resource"] == "UNIPROT"),
        "by_organism": {org: dict(v) for org, v in by_org.items()},
        "by_type": dict(collections.Counter(r["defect_type"] for r in rows)),
        "by_confidence": dict(collections.Counter(r["confidence"] for r in rows)),
    }


def main() -> None:
    """Write the tally and the defect list as YAML."""
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--genes-dir", type=Path, default=Path("genes"))
    p.add_argument("-o", "--output", type=Path, required=True)
    args = p.parse_args()
    rows = list(iter_defects(args.genes_dir))
    out = {"summary": summarise(rows), "defects": rows}
    args.output.write_text(yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")
    print(yaml.safe_dump(out["summary"], sort_keys=False))


if __name__ == "__main__":
    main()
