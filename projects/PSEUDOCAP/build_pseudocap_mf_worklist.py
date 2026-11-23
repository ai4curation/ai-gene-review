"""Build the tier-3 PseudoCAP worklist: unreviewed proteins with experimental MF rows.

Tiers 1 and 2 (``build_iba_seed_worklist.py``) selected PAO1 proteins that seed a
PAINT node, because an error there propagates. That set is reviewed. The plan's
next step is "the rest of the PseudoCAP corpus (2,069 rows on PAO1 in QuickGO),
prioritising IMP rows on molecular-function terms", and this builds that list.

Why IMP-on-MF first: an IMP is a mutant phenotype, which is evidence about what
the cell does without the gene, not about what the protein does. Using it for a
*molecular function* asserts an activity from an absence, so the row is either
well-grounded in a paper that also assayed the protein, or it is the kind of
over-annotation this project exists to find. Either way it repays reading.

Entries already reviewed stay in the list with their ``review_folder`` set, so the
file doubles as a progress record rather than shrinking as work lands; unreviewed
entries sort first.

Inputs are the cached QuickGO slices under ``.cache/paint/`` that the IBA-seed
builder already downloads (delete the folder to refresh):

    pseudocap.tsv  PAO1 rows whose ASSIGNED BY is PseudoCAP
    pao1.tsv       UniProt entry metadata (symbol, locus, reviewed flag)

Usage::

    uv run python projects/PSEUDOCAP/build_pseudocap_mf_worklist.py
    uv run python projects/PSEUDOCAP/build_pseudocap_mf_worklist.py --all-aspects
"""

from __future__ import annotations

import argparse
import csv
import glob
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".cache" / "paint"
OUT = Path(__file__).resolve().parent / "pseudocap_mf_worklist.yaml"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP"}


def reviewed_accessions() -> dict[str, str]:
    """UniProt accession -> review folder, for every PSEAE review on disk."""
    out: dict[str, str] = {}
    for path in glob.glob(str(ROOT / "genes" / "PSEAE" / "*" / "*-ai-review.yaml")):
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                if line.startswith("id: "):
                    out[line.split(None, 1)[1].strip()] = Path(path).parent.name
                    break
    return out


def read_rows(name: str) -> list[dict[str, str]]:
    with open(CACHE / name, encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def entry_metadata() -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in read_rows("pao1.tsv"):
        out[row["Entry"]] = {
            "locus": (row.get("Gene Names (ordered locus)") or "").split()[0]
            if row.get("Gene Names (ordered locus)")
            else "",
            "uniprot_reviewed": row.get("Reviewed") == "reviewed",
            "protein_name": row.get("Protein names", ""),
        }
    return out


def build(all_aspects: bool) -> dict[str, Any]:
    reviewed = reviewed_accessions()
    meta = entry_metadata()

    by_acc: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_rows("pseudocap.tsv"):
        by_acc[row["GENE PRODUCT ID"]].append(row)

    aspects = {"F", "P", "C"} if all_aspects else {"F"}
    entries: list[dict[str, Any]] = []
    for acc, rows in by_acc.items():
        imp_mf = [
            r
            for r in rows
            if r["GO EVIDENCE CODE"] == "IMP" and r["GO ASPECT"] in aspects
        ]
        if not imp_mf:
            continue
        info = meta.get(acc, {})
        entries.append(
            {
                "uniprot": acc,
                "symbol": rows[0]["SYMBOL"],
                "locus": info.get("locus", ""),
                "uniprot_reviewed": info.get("uniprot_reviewed", False),
                "protein_name": info.get("protein_name", ""),
                # Selection is a fixed snapshot of the corpus, like the IBA-seed
                # worklist: entries stay listed once reviewed so the queue shows
                # progress and the project page keeps matching it.
                "review_folder": reviewed.get(acc),
                "pseudocap_rows": len(rows),
                "experimental_rows": sum(
                    r["GO EVIDENCE CODE"] in EXPERIMENTAL for r in rows
                ),
                "imp_mf_rows": [
                    {
                        "term": r["GO TERM"],
                        "qualifier": r["QUALIFIER"],
                        "reference": r["REFERENCE"],
                    }
                    for r in sorted(imp_mf, key=lambda r: (r["GO TERM"], r["REFERENCE"]))
                ],
                "references": sorted({r["REFERENCE"] for r in rows}),
            }
        )

    # Most IMP-on-MF rows first: those assert the most activity from phenotype.
    entries.sort(
        key=lambda e: (
            e["review_folder"] is not None,
            -len(e["imp_mf_rows"]),
            -e["pseudocap_rows"],
            e["symbol"],
        )
    )

    shared = defaultdict(list)
    for entry in entries:
        for row in entry["imp_mf_rows"]:
            shared[(row["term"], row["reference"])].append(entry["symbol"])

    return {
        "generator": "projects/PSEUDOCAP/build_pseudocap_mf_worklist.py",
        "source": "QuickGO PseudoCAP rows for PAO1, cached at .cache/paint/pseudocap.tsv",
        "summary": {
            "pseudocap_rows": sum(len(v) for v in by_acc.values()),
            "pseudocap_proteins": len(by_acc),
            "already_reviewed": sum(1 for a in by_acc if a in reviewed),
            "unreviewed": sum(1 for a in by_acc if a not in reviewed),
            "selected": len(entries),
            "selected_reviewed": sum(1 for e in entries if e["review_folder"]),
            "selected_remaining": sum(1 for e in entries if not e["review_folder"]),
            "aspects": sorted(aspects),
        },
        # Groups worth reviewing together: one paper asserting one term across
        # several proteins is usually one judgement (a complex, or an operon).
        "shared_claims": [
            {"term": term, "reference": ref, "symbols": sorted(syms)}
            for (term, ref), syms in sorted(shared.items())
            if len(syms) > 1
        ],
        "genes": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--all-aspects",
        action="store_true",
        help="select IMP rows on any aspect, not only molecular function",
    )
    args = parser.parse_args()

    data = build(args.all_aspects)
    OUT.write_text(
        yaml.safe_dump(data, sort_keys=False, width=100, allow_unicode=True),
        encoding="utf-8",
    )
    print(f"wrote {OUT.relative_to(ROOT)}")
    for key, value in data["summary"].items():
        print(f"  {key}: {value}")
    print(f"  shared_claims: {len(data['shared_claims'])}")


if __name__ == "__main__":
    main()
