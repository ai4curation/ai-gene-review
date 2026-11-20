"""Which accessible-surfaceome catalog genes / SurfaceBench genes have an ai-gene-review human review?"""
import csv
import collections
from common import DATA, RESULTS, benchmark, reviewed_human

ours = reviewed_human()
syms = set(ours.values())
rows = list(csv.DictReader(open(DATA / "deep-dive-preset-membership.tsv"), delimiter="\t"))
hit = [r for r in rows if r["uniprot_acc"] in ours or r["gene_symbol"] in syms]
tiers = collections.Counter(r["deep_dive_tier"] for r in rows)
htiers = collections.Counter(r["deep_dive_tier"] for r in hit)
print(f"catalog deep-dive genes: {len(rows)}  reviewed: {len(hit)}")
for t in ["canonical", "likely", "low", "uncertain", "no"]:
    print(f"  {t:10s} {htiers[t]:5d} / {tiers[t]}")
with open(RESULTS / "catalog_overlap.tsv", "w") as f:
    f.write("gene\tuniprot\tdeep_dive_tier\treview_folder\n")
    for r in sorted(hit, key=lambda r: (r["deep_dive_tier"], r["gene_symbol"])):
        f.write(f"{r['gene_symbol']}\t{r['uniprot_acc']}\t{r['deep_dive_tier']}\t{ours.get(r['uniprot_acc'], r['gene_symbol'])}\n")
truth = benchmark()
missing = sorted(r["gene_symbol"] for a, r in truth.items() if a not in ours and r["gene_symbol"] not in syms)
print(f"SurfaceBench genes: {len(truth)}  reviewed: {len(truth) - len(missing)}  missing: {' '.join(missing) or '-'}")
