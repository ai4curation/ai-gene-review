#!/usr/bin/env python3
"""Build a positive-control query set of well-characterised SwissProt proteins.

Used to check that the local re-implementation of the ProTrek protein encoder
reproduces sensible retrieval behaviour before the benchmark run is trusted.
These proteins are reviewed SwissProt entries and are almost certainly inside
ProTrek's training set, so the expected result is that the top retrieved GO
sentence is the protein's textbook function; this is a smoke test of the
pipeline, not a measure of predictive skill.

Usage: uv run python projects/PROTREK_EVALUATION/build_controls.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).parent))
from build_inputs import parse_uniprot  # noqa: E402

CONTROLS = [
    ("human", "SOD1"),
    ("human", "GPX4"),
    ("human", "TP53"),
    ("ECOLI", "DnaK"),
    ("ECOLI", "GroEL"),
]
OUT = Path(__file__).parent / "control_sequences.tsv"


def main() -> int:
    lines = ["accession\tspecies_dir\torganism\ttaxon_id\tlength\tprotein_name\tpred_category\tsequence"]
    for species, gene in CONTROLS:
        flat = ROOT / "genes" / species / gene / f"{gene}-uniprot.txt"
        if not flat.exists():
            print(f"WARNING: missing {flat}", file=sys.stderr)
            continue
        rec = parse_uniprot(flat)
        acc = ""
        for line in flat.read_text().splitlines():
            if line.startswith("AC   "):
                acc = line[5:].split(";")[0].strip()
                break
        lines.append("\t".join([acc, species, rec["organism"], rec["taxon"],
                                str(len(rec["sequence"])), gene, "control", rec["sequence"]]))
    OUT.write_text("\n".join(lines) + "\n")
    print(f"wrote {len(lines) - 1} control sequences to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
