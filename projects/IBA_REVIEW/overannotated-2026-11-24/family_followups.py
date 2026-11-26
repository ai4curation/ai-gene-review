"""List what the batch records say about family reviews, as family_review_followups.tsv.

Reviewers in this pass did not edit family reviews (interpro/panther/). Where one disagreed
with a family review, or found it describing a gene review that has since changed, the
record says so in its notes. This pulls those sentences out, one line per family and row,
so the family reviews can be brought up to date in one pass.

    uv run python projects/IBA_REVIEW/overannotated-2026-11-24/family_followups.py
"""

from __future__ import annotations

import csv
import glob
import re
from pathlib import Path

import yaml

HERE = Path(__file__).parent


def main() -> None:
    out = []
    for path in sorted(glob.glob(str(HERE / "batches" / "batch-*.yaml"))):
        for gene in yaml.safe_load(open(path))["genes"]:
            for row in gene["rows"]:
                text = " ".join(str(row.get("notes") or "").split())
                for sentence in re.split(r"(?<=\.)\s+(?=[A-Z])", text):
                    if not re.search(r"family review", sentence, re.I):
                        continue
                    fams = sorted(set(re.findall(r"PTHR\d{5}", sentence))) or [row.get("family")]
                    for fam in fams:
                        out.append([fam, Path(path).stem, "/".join(gene["gene_file"].split("/")[1:3]),
                                    row["go_id"], sentence])
    out.sort()
    with open(HERE / "family_review_followups.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["family", "batch", "gene", "go_id", "note"])
        w.writerows(out)
    print(len(out), "notes on", len({r[0] for r in out}), "families")


if __name__ == "__main__":
    main()
