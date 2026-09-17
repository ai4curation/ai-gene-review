"""Provenance audit of the human ARFGEF2 (BIG2) GO annotation set.

Four questions, all answered from live QuickGO / UniProt data:

A. **Rat funnel.** How many human GOA rows are projections of rat Arfgef2
   (Q7TSU1), which rat annotations are they projections *of*, and how many
   distinct primary references do those rat annotations rest on? A large block
   of human rows resting on one donor paper is a single point of failure.

B. **Paralog check on each donor reference.** For every primary reference behind
   the rat funnel, which entities does that reference annotate anywhere in GOA?
   If a reference's human annotations all land on the *paralog*, a row on this
   gene is a paralog attribution, not independent evidence.

C. **Projection discriminator.** For every PMID cited in ARFGEF2's own GOA rows,
   how many distinct entities does that reference annotate? A reference that
   annotates a complex plus every subunit with identical evidence is a
   projection, not N independent findings. Entities are counted as a distinct
   set of gene-product ids, never as an annotation total.

D. **Coverage gap.** Which primary papers about this protein - taken from the
   union of the UniProt entry's own RX PubMed list and the affinage
   deep-research citation list, never from a hand-assigned list - produced
   **zero** GO annotations anywhere in GOA?

Outputs `provenance_audit.json` and prints a human-readable summary.
A fresh run must reproduce `RESULTS.md`; see `audit_claims.py`.

Run: uv run python provenance_audit.py
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

from uniprot import EXPERIMENTAL, quickgo_by_gene, quickgo_by_reference

HERE = Path(__file__).parent
GENE_DIR = HERE.parent
GOA = GENE_DIR / "ARFGEF2-goa.tsv"
UNIPROT = GENE_DIR / "ARFGEF2-uniprot.txt"
AFFINAGE = GENE_DIR / "ARFGEF2-deep-research-affinage.md"

SUBJECT = "Q9Y6D5"          # human ARFGEF2 / BIG2
RAT_DONOR = "Q7TSU1"        # rat Arfgef2 / BIG2, the Compara + ISS donor
PARALOG = "Q9Y6D6"          # human ARFGEF1 / BIG1

PMID_RE = re.compile(r"PMID:(\d+)")


def _require(path: Path, fix: str) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"{path} is missing. Regenerate it with: {fix}")
    return path


def load_goa() -> list[dict[str, str]]:
    with _require(GOA, "just fetch-gene human ARFGEF2").open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def uniprot_pmids() -> set[str]:
    """PubMed ids from the UniProt entry's own RX lines."""
    text = _require(UNIPROT, "just fetch-gene human ARFGEF2").read_text()
    return set(re.findall(r"^RX\s+PubMed=(\d+);", text, flags=re.MULTILINE))


def affinage_pmids() -> set[str]:
    """PubMed ids cited by the affinage deep-research record.

    Non-numeric ids (e.g. `PMID:bio_10.1101_...`, a bioRxiv DOI in a PMID-shaped
    field) are excluded by the numeric regex and reported separately.
    """
    text = _require(
        AFFINAGE,
        "uv run python projects/AFFINAGE_EVALUATION/affinage_deep_research.py human ARFGEF2 --write",
    ).read_text()
    numeric = set(PMID_RE.findall(text))
    nonnumeric = set(re.findall(r"PMID:([A-Za-z_][\w./-]*)", text))
    return numeric, nonnumeric


def rat_funnel(goa: list[dict[str, str]]) -> dict:
    """A. Which human rows are projections of rat Arfgef2, and of what?"""
    human_rows = []
    for i, row in enumerate(goa, start=1):
        if RAT_DONOR in (row["WITH/FROM"] or ""):
            human_rows.append(
                {
                    "goa_row": i,
                    "go_id": row["GO TERM"],
                    "go_name": row["GO NAME"],
                    "aspect": row["GO ASPECT"],
                    "evidence": row["GO EVIDENCE CODE"],
                    "reference": row["REFERENCE"],
                }
            )

    rat = quickgo_by_gene(RAT_DONOR)
    by_term: dict[str, list[dict]] = defaultdict(list)
    for a in rat:
        by_term[a["goId"]].append(a)

    for hr in human_rows:
        donors = by_term.get(hr["go_id"], [])
        exp = [d for d in donors if (d.get("goEvidence") or "") in EXPERIMENTAL]
        hr["rat_annotations"] = len(donors)
        hr["rat_experimental"] = len(exp)
        hr["rat_evidence_codes"] = sorted({d.get("goEvidence") or "?" for d in donors})
        hr["rat_primary_references"] = sorted(
            {d["reference"] for d in exp if d["reference"].startswith("PMID:")}
        )
        hr["rat_assigned_by"] = sorted({d["assignedBy"] for d in exp})

    all_primary = sorted({r for hr in human_rows for r in hr["rat_primary_references"]})
    return {
        "human_rows_from_rat_donor": human_rows,
        "n_human_rows": len(human_rows),
        "n_distinct_terms": len({hr["go_id"] for hr in human_rows}),
        "distinct_rat_primary_references": all_primary,
    }


def reference_entities(pmid: str) -> dict:
    """C. Entity/annotation profile of one reference across all of GOA."""
    rows = quickgo_by_reference(pmid)
    entities = {r["geneProductId"] for r in rows}
    on_subject = [r for r in rows if r["geneProductId"] == f"UniProtKB:{SUBJECT}"]
    on_paralog = [r for r in rows if r["geneProductId"] == f"UniProtKB:{PARALOG}"]
    return {
        "pmid": pmid,
        "n_annotations": len(rows),
        "n_entities": len(entities),
        "entities": sorted(entities),
        "terms": sorted({r["goId"] for r in rows}),
        "n_on_subject": len(on_subject),
        "subject_terms": sorted({r["goId"] for r in on_subject}),
        "n_on_paralog": len(on_paralog),
        "paralog_terms": sorted({r["goId"] for r in on_paralog}),
        "evidence_codes": sorted({r.get("goEvidence") or "?" for r in rows}),
    }


def main() -> None:
    goa = load_goa()
    goa_pmids = sorted({m.group(1) for row in goa
                        for m in [PMID_RE.match(row["REFERENCE"] or "")] if m})

    funnel = rat_funnel(goa)

    # B + C: profile every reference that matters - the gene's own GOA
    # references plus the primary references behind the rat funnel.
    profile_pmids = sorted(set(goa_pmids) | set(
        r.split(":", 1)[1] for r in funnel["distinct_rat_primary_references"]
    ))
    profiles = {p: reference_entities(p) for p in profile_pmids}

    # D: coverage gap over the derived literature set.
    lit_numeric, lit_nonnumeric = affinage_pmids()
    literature = sorted(uniprot_pmids() | lit_numeric)
    coverage = []
    for p in literature:
        prof = profiles.get(p) or reference_entities(p)
        profiles[p] = prof
        coverage.append(
            {"pmid": p, "n_annotations": prof["n_annotations"],
             "n_on_subject": prof["n_on_subject"],
             "subject_terms": prof["subject_terms"]}
        )
    zero_anywhere = [c["pmid"] for c in coverage if c["n_annotations"] == 0]
    zero_on_subject = [c["pmid"] for c in coverage if c["n_on_subject"] == 0]

    out = {
        "subject": SUBJECT,
        "rat_donor": RAT_DONOR,
        "paralog": PARALOG,
        "goa_rows": len(goa),
        "goa_pmids": goa_pmids,
        "rat_funnel": funnel,
        "reference_profiles": profiles,
        "literature_pmids": literature,
        "literature_nonnumeric_pmid_tokens": sorted(lit_nonnumeric),
        "coverage": coverage,
        "pmids_with_zero_go_annotations_anywhere": zero_anywhere,
        "pmids_with_zero_annotations_on_subject": zero_on_subject,
    }
    (HERE / "provenance_audit.json").write_text(json.dumps(out, indent=2) + "\n")

    print(f"GOA rows: {len(goa)}")
    print(f"A. human rows projected from rat {RAT_DONOR}: {funnel['n_human_rows']} "
          f"covering {funnel['n_distinct_terms']} distinct GO terms")
    print(f"   distinct rat primary references behind them: "
          f"{funnel['distinct_rat_primary_references']}")
    for hr in funnel["human_rows_from_rat_donor"]:
        print(f"   row {hr['goa_row']:>2} {hr['go_id']} {hr['go_name'][:34].ljust(34)} "
              f"{hr['evidence']:<4} <- rat {hr['rat_evidence_codes']} "
              f"{hr['rat_primary_references']}")
    print()
    print("B/C. reference profiles (n_entities / n_annotations / on subject / on paralog):")
    for p in sorted(profiles):
        pr = profiles[p]
        print(f"   PMID:{p:<9} entities={pr['n_entities']:<3} ann={pr['n_annotations']:<5} "
              f"subject={pr['n_on_subject']:<2} paralog={pr['n_on_paralog']:<2} "
              f"{pr['evidence_codes']}")
    print()
    print(f"D. literature PMIDs (UniProt RX + affinage citations): {len(literature)}")
    print(f"   with ZERO GO annotations anywhere in GOA: {len(zero_anywhere)}")
    print(f"   {zero_anywhere}")
    print(f"   with zero annotations on {SUBJECT}: {len(zero_on_subject)}")
    if lit_nonnumeric:
        print(f"   non-numeric PMID-shaped tokens in the affinage record "
              f"(NOT PubMed ids): {sorted(lit_nonnumeric)}")


if __name__ == "__main__":
    main()
