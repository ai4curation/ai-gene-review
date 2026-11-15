"""Tally the description-text source defects recorded by the MOD descriptions project.

Counts the WRONG_STATEMENT, OUTDATED_STATEMENT and MISSING_STATEMENT defects (and
WRONG_REFERENCE defects on a cited file) that the worm, yeast and fly reviews record
against MOD (WormBase, SGD, FlyBase) and UniProt text, and lists each one with its
quoted source sentence and evidence. Other source defects, mostly on GO annotations,
are not counted.

``confidence`` is the reviewer's judgement recorded on the defect (CONFIRMED or
PROBABLE). It is reported separately from ``with_paper_evidence``, the defects whose
supporting evidence includes a quote from a PMID: the two do not coincide.

Usage:
    uv run python projects/MOD_DESCRIPTIONS/defect_tally.py --date 2026-11-15 \
        -o projects/MOD_DESCRIPTIONS/defect-tally.yaml
"""

import argparse
import collections
from datetime import date
from pathlib import Path
from typing import Any, Dict, Iterator, List

import yaml

ORGANISMS = ("worm", "yeast", "DROME")
STATEMENT_TYPES = ("WRONG_STATEMENT", "OUTDATED_STATEMENT", "MISSING_STATEMENT")
MOD_RESOURCES = ("WORMBASE", "SGD", "FLYBASE")
RESOURCES = MOD_RESOURCES + ("UNIPROT",)


def iter_defects(genes_dir: Path) -> Iterator[Dict[str, Any]]:
    """Yield one row per description-text defect in the worm, yeast and fly reviews."""
    for org in ORGANISMS:
        for review in sorted((genes_dir / org).glob("*/*-ai-review.yaml")):
            data = yaml.safe_load(review.read_text(encoding="utf-8")) or {}
            for ref in data.get("references") or []:
                ref_id = str(ref.get("id", ""))
                for sd in (ref.get("reference_review") or {}).get("source_defects") or []:
                    kind = str(sd.get("defect_type", ""))
                    if sd.get("resource") not in RESOURCES:
                        continue
                    if kind not in STATEMENT_TYPES and not (kind == "WRONG_REFERENCE" and ref_id.startswith("file:")):
                        continue
                    evidence = [e for e in sd.get("supported_by") or [] if isinstance(e, dict)]
                    yield {
                        "organism": org,
                        "gene": review.parent.name,
                        "reference_id": ref_id,
                        "resource": sd.get("resource"),
                        "slot": sd.get("slot"),
                        "defect_type": kind,
                        "requested_change": sd.get("requested_change"),
                        "confidence": sd.get("confidence"),
                        "record": sd.get("record"),
                        "asserted_value": sd.get("asserted_value"),
                        "explanation": sd.get("explanation"),
                        "with_paper_evidence": any(str(e.get("reference_id", "")).startswith("PMID:") for e in evidence),
                        "evidence": [
                            {"reference_id": e.get("reference_id"), "supporting_text": e.get("supporting_text")}
                            for e in evidence
                        ],
                    }


def summarise(rows: List[Dict[str, Any]], as_of: str) -> Dict[str, Any]:
    """Count defects by organism, resource, type, confidence and paper evidence."""
    by_org: Dict[str, Dict[str, int]] = collections.defaultdict(lambda: collections.defaultdict(int))
    for r in rows:
        by_org[r["organism"]][r["resource"]] += 1
        by_org[r["organism"]]["confidence_confirmed"] += r["confidence"] == "CONFIRMED"
        by_org[r["organism"]]["with_paper_evidence"] += r["with_paper_evidence"]
    mod_text = sum(1 for r in rows if r["resource"] in MOD_RESOURCES)
    uniprot_text = sum(1 for r in rows if r["resource"] == "UNIPROT")
    assert mod_text + uniprot_text == len(rows), "every counted defect is on MOD or UniProt text"
    return {
        "date": as_of,
        "total": len(rows),
        "mod_text": mod_text,
        "uniprot_text": uniprot_text,
        "with_paper_evidence": sum(r["with_paper_evidence"] for r in rows),
        "by_organism": {org: dict(v) for org, v in by_org.items()},
        "by_type": dict(collections.Counter(r["defect_type"] for r in rows)),
        "by_confidence": dict(collections.Counter(r["confidence"] for r in rows)),
    }


def main() -> None:
    """Write the tally and the defect list as YAML."""
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--genes-dir", type=Path, default=Path("genes"))
    p.add_argument("--date", default=date.today().isoformat(), help="as-of date written to the summary")
    p.add_argument("-o", "--output", type=Path, required=True)
    args = p.parse_args()
    rows = list(iter_defects(args.genes_dir))
    out = {"summary": summarise(rows, args.date), "defects": rows}
    args.output.write_text(yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")
    print(yaml.safe_dump(out["summary"], sort_keys=False))


if __name__ == "__main__":
    main()
