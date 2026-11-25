"""Report PANTHER subfamily placement and PAINT node annotations relevant to ftz-f1 (P33244).

Run from the repository root:
    python3 genes/DROME/ftz-f1__P33244/ftz-f1__P33244-bioinformatics/family_placement.py

Inputs:
  interpro/panther/PTHR24086/PTHR24086-entries.csv  (repo PANTHER member table)
  PTHR24086-paint-slice.tsv  (output of `ai-gene-review fetch-panther-paint PTHR24086`,
                              node-level IBD rows; copied here unmodified)
"""
import csv
from pathlib import Path

HERE = Path(__file__).parent
ENTRIES = Path("interpro/panther/PTHR24086/PTHR24086-entries.csv")
WATCH = ["P33244", "P49867", "Q19345", "Q05192", "Q13285", "O00482"]

with ENTRIES.open() as fh:
    rows = {r["id"]: r for r in csv.DictReader(fh)}
print("## Subfamily placement")
for acc in WATCH:
    r = rows.get(acc)
    if r is None:
        print(f"{acc}\tNOT IN TABLE")
    else:
        print(f"{acc}\t{r['gene']}\t{r['source_tax_name']}\t{r['subfamily']}\t{r['subfamily_name']}")

print("\n## PAINT node-level annotations")
with (HERE / "PTHR24086-paint-slice.tsv").open() as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        print(f"{r['node']}\t{r['go_id']}\t{r['aspect']}\t{r['evidence']}\ttaxon={r['taxon']}\tseeds={r['seeds']}")
