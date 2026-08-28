#!/usr/bin/env python3
"""Build the ProTrek query set for the ARGO139 cohort (the BioReason comparison genes).

ARGO139 is defined by projects/BIOREASON_COMPARISON/genes.csv and is the cohort the
BioReason-Pro / GO-GPT evaluations were scored on. Running ProTrek over the same genes
gives a term-level VDCL comparison on an identical gene set.

Sequences come from each gene's cached UniProt flatfile. The accession actually present
in the cache is recorded alongside the accession the cohort asked for, so input mismatches
(such as the documented worm/csr-1 case) are visible rather than silent.

Usage: uv run python projects/PROTREK_EVALUATION/build_argo139_inputs.py
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).parent))
from build_inputs import parse_uniprot  # noqa: E402

COHORT = ROOT / "projects/BIOREASON_COMPARISON/genes.csv"
OUT = Path(__file__).parent / "argo139_sequences.tsv"


def cached_accession(flat: Path) -> str:
    for line in flat.read_text().splitlines():
        if line.startswith("AC   "):
            return line[5:].split(";")[0].strip()
    return ""


def main() -> int:
    rows = list(csv.DictReader(COHORT.open()))
    out = []
    for r in rows:
        gene, species = r["symbol"], r["species"]
        flat = ROOT / "genes" / species / gene / f"{gene}-uniprot.txt"
        if not flat.exists():
            print(f"WARNING: no flatfile for {species}/{gene}", file=sys.stderr)
            continue
        rec = parse_uniprot(flat)
        acc = cached_accession(flat)
        if not rec["sequence"]:
            print(f"WARNING: no sequence parsed for {species}/{gene}", file=sys.stderr)
            continue
        out.append({
            "accession": acc,
            "cohort_accession": r["uniprot_id"],
            "accession_matches_cohort": str(acc == r["uniprot_id"]),
            "species_dir": species,
            "symbol": gene,
            "organism": rec["organism"],
            "taxon_id": rec["taxon"],
            "length": len(rec["sequence"]),
            "sequence": rec["sequence"],
        })

    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(out)
    bad = [r for r in out if r["accession_matches_cohort"] == "False"]
    print(f"wrote {len(out)} sequences to {OUT}")
    if bad:
        print("accession mismatches (cached record differs from cohort list):")
        for r in bad:
            print(f"  {r['species_dir']}/{r['symbol']}: cohort={r['cohort_accession']} cached={r['accession']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
