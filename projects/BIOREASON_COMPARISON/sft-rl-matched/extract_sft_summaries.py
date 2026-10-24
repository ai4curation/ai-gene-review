#!/usr/bin/env python3
"""Extract BioReason-Pro SFT Functional Summaries for ARGO139 genes from the
HuggingFace ``wanglab/protein_catalogue`` parquet shards.

The catalogue is not committed (about 626 MB). Download the three shards from
https://huggingface.co/datasets/wanglab/protein_catalogue/tree/main/data and pass
their directory with ``--parquet-dir``.

Usage (from repo root):
    uv run python projects/BIOREASON_COMPARISON/sft-rl-matched/extract_sft_summaries.py \
        --parquet-dir /path/to/protein_catalogue/data

Writes ``sft-functional-summaries.tsv`` next to this script: one row per ARGO139
gene whose UniProt accession is present in the catalogue, with the parsed
Functional Summary and a SHA-256 of the full ``generation`` string for provenance.
Nothing is scored here.
"""

import argparse
import csv
import hashlib
import re
from pathlib import Path

import duckdb

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
FS_RE = re.compile(
    r"- Functional Summary:\s*(.*?)(?=\n- (?:UniProt|InterPro|Molecular|Biological|Cellular)|\Z)",
    re.DOTALL,
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parquet-dir", required=True, type=Path)
    ap.add_argument("--out", type=Path, default=HERE / "sft-functional-summaries.tsv")
    args = ap.parse_args()

    genes = list(csv.DictReader(open(PROJECT / "genes.csv")))
    ids = [g["uniprot_id"] for g in genes]
    con = duckdb.connect()
    glob = str(args.parquet_dir / "*.parquet")
    rows = con.execute(
        f"SELECT protein_id, model, organism, generation FROM '{glob}' "
        "WHERE protein_id IN (SELECT unnest(?))",
        [ids],
    ).fetchall()
    by_id = {r[0]: r for r in rows}

    n_found = 0
    with open(args.out, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(
            ["species", "gene", "uniprot_id", "hf_model", "hf_organism",
             "generation_sha256", "functional_summary"]
        )
        for g in genes:
            r = by_id.get(g["uniprot_id"])
            if r is None:
                continue
            _, model, organism, gen = r
            m = FS_RE.search(gen.split("</think>")[-1])
            fs = " ".join(m.group(1).split()) if m else ""
            w.writerow([g["species"], g["symbol"], g["uniprot_id"], model, organism,
                        hashlib.sha256(gen.encode()).hexdigest(), fs])
            n_found += 1
    print(f"{n_found}/{len(genes)} ARGO139 accessions found in catalogue -> {args.out}")


if __name__ == "__main__":
    main()
