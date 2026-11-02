#!/usr/bin/env python3
"""Write the DONKEY40 ProtNLM2 snapshot from fetch_protnlm_api.py output.

Steps:
  1. fetch the 40 selected accessions with the project's fetcher:
       python3 projects/PROTNLM_EVALUATION/donkey40/snapshot_donkey40.py --accessions-file accs.txt
     prints the accession list from selection.yaml; then
       python3 projects/PROTNLM_EVALUATION/fetch_protnlm_api.py --accessions accs.txt --out-dir FETCHDIR
  2. python3 projects/PROTNLM_EVALUATION/donkey40/snapshot_donkey40.py --fetch-dir FETCHDIR

Step 2 copies the fetcher's three tables next to this script as
donkey40-entries.tsv, donkey40-predictions.tsv and donkey40-evidence.tsv,
sorted by accession (stable, so each entry keeps the fetcher's row order), and
adds a gene_symbol column (from selection.yaml) after the accession in the
entries and predictions tables. Nothing else is changed.
"""
from __future__ import annotations

import argparse
import csv
import os

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch-dir", help="output directory of fetch_protnlm_api.py")
    ap.add_argument("--accessions-file", help="write the selected accessions here and stop")
    args = ap.parse_args()
    records = yaml.safe_load(open(os.path.join(HERE, "selection.yaml")))["records"]
    symbol = {r["donkey_accession"]: r["gene_symbol"] for r in records}
    if args.accessions_file:
        with open(args.accessions_file, "w") as fh:
            fh.write("".join(f"{a}\n" for a in symbol))
        return
    if not args.fetch_dir:
        ap.error("give --fetch-dir or --accessions-file")
    for src, dst, add_symbol in (("entries.tsv", "donkey40-entries.tsv", True),
                                 ("predictions.tsv", "donkey40-predictions.tsv", True),
                                 ("evidence.tsv", "donkey40-evidence.tsv", False)):
        with open(os.path.join(args.fetch_dir, src)) as fh:
            rows = list(csv.reader(fh, delimiter="\t"))
        header, body = rows[0], sorted(rows[1:], key=lambda r: r[0])
        missing = {r[0] for r in body} - set(symbol)
        if missing:
            raise SystemExit(f"{src}: accessions not in selection.yaml: {sorted(missing)}")
        if add_symbol:
            header = header[:1] + ["gene_symbol"] + header[1:]
            body = [r[:1] + [symbol[r[0]]] + r[1:] for r in body]
        with open(os.path.join(HERE, dst), "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(header)
            w.writerows(body)
        print(f"wrote {dst}: {len(body)} rows")


if __name__ == "__main__":
    main()
