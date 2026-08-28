#!/usr/bin/env python3
"""Build the ProTrek query input table for the ARGO-ProtNLM-50 benchmark.

Reads the benchmark accession list from projects/PROTNLM_EVALUATION/argo_protnlm_50.csv,
locates each protein's cached UniProt flatfile under genes/<SPECIES>/<ACC>/, and emits
a TSV with accession, species dir, taxon and amino-acid sequence.

Usage: uv run python projects/PROTREK_EVALUATION/build_inputs.py
"""
import csv
import glob
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BENCH = ROOT / "projects/PROTNLM_EVALUATION/argo_protnlm_50.csv"
OUT = Path(__file__).parent / "argo50_sequences.tsv"


def parse_uniprot(path: Path) -> dict:
    """Extract accession, organism, OX taxon and sequence from a UniProt flatfile."""
    seq_lines, in_seq = [], False
    rec = {"organism": "", "taxon": ""}
    for line in path.read_text().splitlines():
        if line.startswith("SQ   "):
            in_seq = True
            continue
        if line.startswith("//"):
            in_seq = False
            continue
        if in_seq:
            seq_lines.append(line.replace(" ", "").strip())
        elif line.startswith("OS   "):
            rec["organism"] += line[5:].strip().rstrip(".")
        elif line.startswith("OX   NCBI_TaxID="):
            rec["taxon"] = line[len("OX   NCBI_TaxID="):].split(";")[0].split()[0]
    rec["sequence"] = "".join(seq_lines)
    return rec


def main() -> int:
    rows = list(csv.DictReader(BENCH.open()))
    out = []
    for r in rows:
        acc = r["accession"]
        hits = glob.glob(str(ROOT / "genes" / "*" / acc / f"{acc}-uniprot.txt"))
        if not hits:
            print(f"WARNING: no uniprot flatfile for {acc}", file=sys.stderr)
            continue
        p = Path(hits[0])
        rec = parse_uniprot(p)
        if not rec["sequence"]:
            print(f"WARNING: no sequence parsed for {acc}", file=sys.stderr)
            continue
        out.append({
            "accession": acc,
            "species_dir": p.parent.parent.name,
            "organism": rec["organism"] or r["organism"],
            "taxon_id": rec["taxon"],
            "length": len(rec["sequence"]),
            "protein_name": r["protein_name"],
            "pred_category": r["pred_category"],
            "sequence": rec["sequence"],
        })

    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(out)
    print(f"wrote {len(out)} sequences to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
