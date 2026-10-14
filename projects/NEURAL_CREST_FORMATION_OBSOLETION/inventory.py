"""Inventory of GOA annotations to GO:0014029 (neural crest formation) and its
regulation terms, for the NEURAL_CREST_FORMATION_OBSOLETION proposal.

Downloads exact (non-propagated) annotations from QuickGO and writes:
  projects/NEURAL_CREST_FORMATION_OBSOLETION/annotations.tsv  (all rows)
  projects/NEURAL_CREST_FORMATION_OBSOLETION/summary.md       (counts)

Usage: uv run python projects/NEURAL_CREST_FORMATION_OBSOLETION/inventory.py
"""
import collections
import csv
import io
import pathlib
import urllib.request

TERMS = ["GO:0014029", "GO:0090299", "GO:0090300", "GO:0090301"]
FIELDS = "geneProductId,symbol,taxonId,qualifier,goId,goName,evidenceCode,goEvidence,reference,withFrom,assignedBy,date"
URL = ("https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?goId={t}&goUsage=exact"
       "&downloadLimit=50000&selectedFields=" + FIELDS)
NAMES = {"GO:0014029": "neural crest formation", "GO:0090299": "regulation of neural crest formation",
         "GO:0090300": "positive regulation of neural crest formation",
         "GO:0090301": "negative regulation of neural crest formation"}
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
OUT = pathlib.Path(__file__).resolve().parent


def fetch(term):
    req = urllib.request.Request(URL.format(t=term), headers={"Accept": "text/tsv"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return list(csv.DictReader(io.StringIO(r.read().decode()), delimiter="\t"))


def main():
    rows = [r for t in TERMS for r in fetch(t)]
    with open(OUT / "annotations.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    lines = ["# GO:0014029 annotation inventory (generated; do not edit)", ""]
    for t in TERMS:
        rs = [r for r in rows if r["GO TERM"] == t]
        exp = [r for r in rs if r["GO EVIDENCE CODE"] in EXPERIMENTAL]
        lines.append(f"## {t} {NAMES[t]}")
        lines.append(f"- rows: {len(rs)}; experimental: {len(exp)} "
                     f"({len({r['GENE PRODUCT ID'] for r in exp})} gene products, "
                     f"{len({r['REFERENCE'] for r in exp})} references)")
        for k in ["GO EVIDENCE CODE", "ASSIGNED BY", "TAXON ID"]:
            c = collections.Counter(r[k] for r in rs).most_common(10)
            lines.append(f"- by {k.lower()}: " + ", ".join(f"{a} {b}" for a, b in c))
        rules = collections.Counter(w for r in rs if r["REFERENCE"] == "GO_REF:0000117"
                                    for w in r["WITH/FROM"].split("|") if w.startswith("ARBA"))
        if rules:
            lines.append("- ARBA rules (GO_REF:0000117): " + ", ".join(f"{a} {b}" for a, b in rules.most_common()))
        lines.append("")
    (OUT / "summary.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {len(rows)} rows")


if __name__ == "__main__":
    main()
