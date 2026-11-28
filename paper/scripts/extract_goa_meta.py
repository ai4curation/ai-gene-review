"""Collect aspect / assigned_by / date for each GOA row behind the reviews.

Output: paper/data/goa_meta.tsv keyed by (id, term_id, evidence_type, reference).
"""
import csv, glob, os, sys
from concurrent.futures import ProcessPoolExecutor

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "paper", "data", "goa_meta.tsv")
ASPECT = {"biological_process": "BP", "molecular_function": "MF", "cellular_component": "CC",
          "P": "BP", "F": "MF", "C": "CC"}

def one(path):
    rows = []
    try:
        with open(path, newline="") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                rows.append((r.get("GENE PRODUCT ID"), r.get("GO TERM"), r.get("GO EVIDENCE CODE"),
                             r.get("REFERENCE"), ASPECT.get(r.get("GO ASPECT"), r.get("GO ASPECT")),
                             r.get("ASSIGNED BY"), r.get("DATE"), r.get("QUALIFIER")))
    except Exception:
        pass
    return rows

def main():
    files = sorted(glob.glob(os.path.join(ROOT, "genes", "*", "*", "*-goa.tsv")))
    seen = {}
    with ProcessPoolExecutor() as ex:
        for rows in ex.map(one, files, chunksize=50):
            for r in rows:
                seen.setdefault(r[:4], r)
    with open(OUT, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["id", "term_id", "evidence_type", "reference", "aspect", "assigned_by", "date", "qualifier"])
        w.writerows(seen.values())
    print(f"{len(seen)} GOA rows from {len(files)} files", file=sys.stderr)

if __name__ == "__main__":
    main()
